# Decision Report

- generated_at: 2026-07-06T17:31:20.108732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8404**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8404, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.72% | **+0.40%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_9PCT | 4/20 | 20.0% | +0.29% | **+0.06%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.48% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.42% | **+1.45%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2624件 (Win 832 / Loss 887 / Flat 905) / skip 2341件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1176件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T17:31:13.995950+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=63880.2
- Funnel: target 841 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUR/USDT:USDT | +21.75% | $1,923,916.62 |
| ANSEM/USDT:USDT | +19.60% | $3,691,951.10 |
| ALLO/USDT:USDT | +12.29% | $12,015,252.11 |
| EDGE/USDT:USDT | +5.37% | $1,074,181.96 |
| HMSTR/USDT:USDT | +4.72% | $4,035,560.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.48% | +4.22% |
| ALLO/USDT:USDT | below_1h_threshold | +3.66% | +3.40% |
| BEAT/USDT:USDT | below_1h_threshold | +2.65% | +2.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.54% | +2.28% |
| BLUR/USDT:USDT | below_1h_threshold | +2.40% | +2.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
