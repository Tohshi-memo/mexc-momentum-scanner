# Decision Report

- generated_at: 2026-07-01T18:08:50.119865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8003**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8003, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.51% | **+0.10%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.20% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.40% | **-0.04%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.30% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.18% | **+0.59%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.88% | **+0.56%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.76% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$268.36** / 初期 $100.00 (+168.36%)
- 確定: 2400件 (Win 732 / Loss 794 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $268.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.74** / 初期 $100.00 (+6.74%)
- 確定: 520件 (Win 131 / Loss 123 / Flat 266) / skip 894件
- 成長率目線: 平均log +0.000125 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0304 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.74

## 5. Latest Market Context

- 更新: 2026-07-01T18:08:45.199454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=60063.7
- Funnel: target 825 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +10.52% | $1,437,211.44 |
| LIT/USDT:USDT | +6.71% | $3,528,198.78 |
| RIF/USDT:USDT | +6.01% | $2,169,935.85 |
| AIGENSYN/USDT:USDT | +5.81% | $6,564,445.01 |
| BILL/USDT:USDT | +3.10% | $1,856,932.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.26% | +3.43% |
| LAB/USDT:USDT | below_1h_threshold | +2.54% | +2.71% |
| RIF/USDT:USDT | below_1h_threshold | +2.01% | +2.18% |
| GRASS/USDT:USDT | below_1h_threshold | +1.25% | +1.42% |
| ALLO/USDT:USDT | below_1h_threshold | +0.41% | +0.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
