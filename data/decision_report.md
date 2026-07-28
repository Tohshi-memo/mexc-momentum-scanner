# Decision Report

- generated_at: 2026-07-28T21:21:33.676270+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9728**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9728, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.21% | **-1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_BB3S | 11/18 | 61.1% | +0.87% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.48% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.24% | **+2.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.48% | **+1.73%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.63% | **+1.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.95% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$510.78** / 初期 $100.00 (+410.78%)
- 確定: 3498件 (Win 1109 / Loss 1134 / Flat 1255) / skip 2791件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $510.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1913件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1695 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.99** / 初期 $100.00 (+10.99%)
- 確定: 746件 (Win 244 / Loss 283 / Flat 219) / pending 6件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000555 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $110.99

## 6. Latest Market Context

- 更新: 2026-07-28T21:21:20.613163+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63891.6
- Funnel: target 904 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +27.40% | $1,402,849.71 |
| ON/USDT:USDT | +19.56% | $39,500,715.78 |
| RIF/USDT:USDT | +17.61% | $4,060,879.72 |
| ZIL/USDT:USDT | +16.15% | $3,412,905.87 |
| BTW/USDT:USDT | +15.56% | $5,835,606.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.62% | +3.62% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.98% | +2.97% |
| RIF/USDT:USDT | below_1h_threshold | +2.73% | +2.73% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.02% | +2.02% |
| CAP/USDT:USDT | below_1h_threshold | +1.63% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
