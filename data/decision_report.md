# Decision Report

- generated_at: 2026-07-01T05:16:46.186924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7952**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7952, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.14% | **+0.12%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.64% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.84%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.37% | **+0.76%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.15% | **+0.58%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.23% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2157件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.84** / 初期 $100.00 (+6.84%)
- 確定: 494件 (Win 127 / Loss 121 / Flat 246) / skip 869件
- 成長率目線: 平均log +0.000134 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0334 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DYDX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.84

## 5. Latest Market Context

- 更新: 2026-07-01T05:16:41.329859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=59284.0
- Funnel: target 823 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYDX/USDT:USDT | +38.88% | $7,691,172.40 |
| TAIKO/USDT:USDT | +24.28% | $1,295,990.63 |
| BTW/USDT:USDT | +22.37% | $11,420,823.88 |
| BEAT/USDT:USDT | +22.10% | $26,882,744.33 |
| TRIA/USDT:USDT | +16.34% | $1,058,913.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.85% | +3.90% |
| O/USDT:USDT | below_1h_threshold | +2.50% | +2.55% |
| XPL/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |
| SPX/USDT:USDT | below_1h_threshold | +0.93% | +0.97% |
| OPG/USDT:USDT | below_1h_threshold | +0.61% | +0.65% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
