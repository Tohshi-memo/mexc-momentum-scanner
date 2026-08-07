# Decision Report

- generated_at: 2026-08-07T06:46:24.705976+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10684**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.51% / filled 20/20。**
- 全期間 MARKET基準: n=10684, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+4.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.51% | **+4.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.51% | **+4.51%** |
| LIMIT_1PCT | 15/20 | 75.0% | +4.55% | **+3.42%** |
| LIMIT_2PCT | 13/20 | 65.0% | +4.86% | **+3.16%** |
| LIMIT_3PCT | 10/20 | 50.0% | +4.31% | **+2.16%** |
| LIMIT_ATR | 6/20 | 30.0% | +3.46% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +2.33% | **+1.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +0.19% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3448件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1455件 (Win 407 / Loss 342 / Flat 706) / skip 2640件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.67** / 初期 $100.00 (+16.67%)
- 確定: 1159件 (Win 371 / Loss 455 / Flat 333) / pending 0件 / skip 996件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000478 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKAMSTOCK/USDT:USDT `MARKET` EXPIRED account +0.09% 残高後 $116.67

## 6. Latest Market Context

- 更新: 2026-08-07T06:46:13.257277+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64329.4
- Funnel: target 960 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +26.37% | $9,878,484.70 |
| ON/USDT:USDT | +21.70% | $9,936,053.34 |
| XAI/USDT:USDT | +21.20% | $1,575,282.96 |
| TWLOSTOCK/USDT:USDT | +17.33% | $1,435,018.50 |
| ZHIPUSTOCK/USDT:USDT | +16.21% | $1,853,743.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +4.73% | +4.70% |
| ON/USDT:USDT | below_1h_threshold | +4.61% | +4.58% |
| STG/USDT:USDT | below_1h_threshold | +3.93% | +3.90% |
| RIVER/USDT:USDT | below_1h_threshold | +3.67% | +3.64% |
| ALLO/USDT:USDT | below_1h_threshold | +3.36% | +3.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
