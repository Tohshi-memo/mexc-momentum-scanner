# Decision Report

- generated_at: 2026-06-26T06:44:40.892332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7611**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7611, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.19% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.62** / 初期 $100.00 (+120.62%)
- 確定: 2138件 (Win 630 / Loss 715 / Flat 793) / skip 2034件
- 成長率目線: 平均log +0.000370 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $220.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 380件 (Win 103 / Loss 100 / Flat 177) / skip 642件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T06:44:35.134898+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=60344.0
- Funnel: target 810 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +29.68% | $6,829,046.63 |
| BEAT/USDT:USDT | +22.49% | $41,549,750.96 |
| AIN/USDT:USDT | +20.75% | $4,247,123.54 |
| BAS/USDT:USDT | +18.81% | $6,602,103.31 |
| IDOL/USDT:USDT | +17.85% | $1,766,507.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +4.48% | +3.78% |
| ARX/USDT:USDT | below_1h_threshold | +3.92% | +3.21% |
| BAS/USDT:USDT | below_1h_threshold | +3.71% | +3.00% |
| G/USDT:USDT | below_1h_threshold | +3.47% | +2.76% |
| OP/USDT:USDT | below_1h_threshold | +3.08% | +2.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
