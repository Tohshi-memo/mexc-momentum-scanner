# Decision Report

- generated_at: 2026-08-07T07:51:27.256630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10687**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.71% / filled 20/20。**
- 全期間 MARKET基準: n=10687, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.96% | **+2.52%** |
| LIMIT_2PCT | 15/20 | 75.0% | +3.28% | **+2.46%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.68% | **+1.61%** |
| LIMIT_ATR | 6/20 | 30.0% | +2.07% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +3.56% | **+1.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.87% | **+0.43%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.70% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3451件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1455件 (Win 407 / Loss 342 / Flat 706) / skip 2643件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.67** / 初期 $100.00 (+16.67%)
- 確定: 1159件 (Win 371 / Loss 455 / Flat 333) / pending 0件 / skip 1001件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000413 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKAMSTOCK/USDT:USDT `MARKET` EXPIRED account +0.09% 残高後 $116.67

## 6. Latest Market Context

- 更新: 2026-08-07T07:51:19.472959+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64342.6
- Funnel: target 960 → liquid 196 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +26.14% | $10,332,813.05 |
| STG/USDT:USDT | +24.22% | $10,433,080.12 |
| SKYAI/USDT:USDT | +19.56% | $62,928,923.81 |
| TAKE/USDT:USDT | +18.46% | $2,798,183.23 |
| TWLOSTOCK/USDT:USDT | +17.30% | $1,463,095.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.39% | +4.30% |
| ACE/USDT:USDT | below_1h_threshold | +4.28% | +4.19% |
| ON/USDT:USDT | below_1h_threshold | +3.19% | +3.10% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.96% | +2.87% |
| BEAT/USDT:USDT | below_1h_threshold | +2.70% | +2.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
