# Decision Report

- generated_at: 2026-07-06T00:00:19.397658+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8357, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.08% | **+0.04%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.15% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +0.85% | **+0.38%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.62% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 65件 (TP 22 / SL 42 / EXP 1)
- 最新: MAGMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.33** / 初期 $100.00 (+220.33%)
- 確定: 2621件 (Win 832 / Loss 885 / Flat 904) / skip 2297件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEROC0MPUTE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $320.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1130件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-06T00:00:13.287596+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63623.4
- Funnel: target 835 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +17.02% | $1,029,488.20 |
| TRB/USDT:USDT | +15.90% | $6,209,141.57 |
| GIGGLE/USDT:USDT | +10.99% | $1,299,106.73 |
| ZEROC0MPUTE/USDT:USDT | +8.68% | $1,625,938.67 |
| TLM/USDT:USDT | +7.91% | $41,222,055.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.02% | +2.16% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.30% | +1.45% |
| UB/USDT:USDT | below_1h_threshold | +1.26% | +1.41% |
| DASH/USDT:USDT | below_1h_threshold | +0.68% | +0.82% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.63% | +0.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
