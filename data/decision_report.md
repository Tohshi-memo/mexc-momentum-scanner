# Decision Report

- generated_at: 2026-06-15T09:38:25.112999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6769**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6769, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.80% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.68% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$178.04** / 初期 $100.00 (+78.04%)
- 確定: 1642件 (Win 429 / Loss 506 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $178.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定: 136件 (Win 26 / Loss 22 / Flat 88) / skip 44件
- 成長率目線: 平均log -0.000103 / 幾何平均 -0.010% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0219 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $98.60

## 5. Latest Market Context

- 更新: 2026-06-15T09:38:16.932744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=65526.0
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +91.17% | $26,208,397.21 |
| ASTEROID/USDT:USDT | +83.21% | $4,476,555.43 |
| CLO/USDT:USDT | +38.86% | $2,264,949.52 |
| PUFFER/USDT:USDT | +34.31% | $1,253,442.27 |
| H/USDT:USDT | +31.60% | $140,158,281.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUFFER/USDT:USDT | below_1h_threshold | +3.42% | +3.56% |
| EVAA/USDT:USDT | below_1h_threshold | +1.98% | +2.13% |
| CLO/USDT:USDT | below_1h_threshold | +1.88% | +2.03% |
| NIL/USDT:USDT | below_1h_threshold | +1.69% | +1.84% |
| WLD/USDT:USDT | below_1h_threshold | +1.25% | +1.40% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
