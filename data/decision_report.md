# Decision Report

- generated_at: 2026-08-04T12:51:41.163250+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10295**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10295, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.84% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.58% | **+2.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3130件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2422件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.04** / 初期 $100.00 (+17.04%)
- 確定: 1060件 (Win 339 / Loss 408 / Flat 313) / pending 6件 / skip 702件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.04

## 6. Latest Market Context

- 更新: 2026-08-04T12:51:30.298935+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63905.6
- Funnel: target 937 → liquid 183 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.1 >= 65=1, 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYS/USDT:USDT | +52.88% | $7,398,189.08 |
| CASHCAT/USDT:USDT | +42.97% | $1,125,040.52 |
| HOME/USDT:USDT | +38.55% | $11,462,062.14 |
| BANK/USDT:USDT | +25.66% | $13,421,281.13 |
| UNITREE/USDT:USDT | +23.42% | $1,590,085.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +4.88% | +4.87% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +4.77% | +4.76% |
| SNXX/USDT:USDT | below_1h_threshold | +4.35% | +4.34% |
| SOXL/USDT:USDT | below_1h_threshold | +3.63% | +3.62% |
| COTI/USDT:USDT | below_1h_threshold | +3.19% | +3.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
