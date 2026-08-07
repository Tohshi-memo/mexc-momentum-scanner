# Decision Report

- generated_at: 2026-08-07T09:51:24.446196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10699**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=10699, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 7/20 | 35.0% | +2.89% | **+1.01%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.83% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.28% | **+1.80%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.66% | **+1.16%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.68% | **+0.76%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.77% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3462件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1455件 (Win 407 / Loss 342 / Flat 706) / skip 2655件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.67** / 初期 $100.00 (+16.67%)
- 確定: 1159件 (Win 371 / Loss 455 / Flat 333) / pending 0件 / skip 1013件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKAMSTOCK/USDT:USDT `MARKET` EXPIRED account +0.09% 残高後 $116.67

## 6. Latest Market Context

- 更新: 2026-08-07T09:51:13.544502+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=64865.0
- Funnel: target 961 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +27.39% | $24,111,100.85 |
| SKYAI/USDT:USDT | +25.74% | $68,520,745.24 |
| CATE/USDT:USDT | +25.07% | $4,399,850.05 |
| HEI/USDT:USDT | +23.94% | $50,873,763.16 |
| ON/USDT:USDT | +21.92% | $11,378,382.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAOISTOCK/USDT:USDT | below_relative_strength | +5.44% | +4.99% |
| HEI/USDT:USDT | below_1h_threshold | +3.73% | +3.29% |
| CATE/USDT:USDT | below_1h_threshold | +3.21% | +2.77% |
| SNXX/USDT:USDT | below_1h_threshold | +2.94% | +2.49% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.71% | +2.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
