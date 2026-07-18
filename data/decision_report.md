# Decision Report

- generated_at: 2026-07-18T07:46:19.070891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8920**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=8920, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.50% | **+0.47%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.66% | **+0.40%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.06% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.48% | **+1.18%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.26% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.15% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.51** / 初期 $100.00 (+265.51%)
- 確定: 3035件 (Win 942 / Loss 965 / Flat 1128) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $365.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.12** / 初期 $100.00 (+11.12%)
- 確定: 882件 (Win 208 / Loss 179 / Flat 495) / skip 1449件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $111.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.40** / 初期 $100.00 (-0.60%)
- 確定: 176件 (Win 55 / Loss 94 / Flat 27) / pending 6件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000283 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.40

## 6. Latest Market Context

- 更新: 2026-07-18T07:46:11.990646+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64000.0
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1, 4h RSI 85.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +55.28% | $55,378,576.06 |
| ESPORTS/USDT:USDT | +37.00% | $13,980,277.92 |
| TRADOOR/USDT:USDT | +33.08% | $2,396,915.96 |
| BSB/USDT:USDT | +11.52% | $1,316,463.35 |
| VVV/USDT:USDT | +11.14% | $2,969,375.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.77% | +1.70% |
| CHIP/USDT:USDT | below_1h_threshold | +1.71% | +1.64% |
| BULLA/USDT:USDT | below_1h_threshold | +1.40% | +1.33% |
| AKE/USDT:USDT | below_1h_threshold | +1.35% | +1.28% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.29% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
