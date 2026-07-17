# Decision Report

- generated_at: 2026-07-17T23:21:20.153907+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8893**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.14% / filled 20/20。**
- 全期間 MARKET基準: n=8893, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.04% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.17% | **-0.13%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.42% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$366.62** / 初期 $100.00 (+266.62%)
- 確定: 3008件 (Win 936 / Loss 956 / Flat 1116) / skip 2446件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $366.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.92** / 初期 $100.00 (+11.92%)
- 確定: 855件 (Win 202 / Loss 174 / Flat 479) / skip 1449件
- 成長率目線: 平均log +0.000132 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0743 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $111.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.67** / 初期 $100.00 (-0.33%)
- 確定: 152件 (Win 49 / Loss 82 / Flat 21) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $99.67

## 6. Latest Market Context

- 更新: 2026-07-17T23:21:10.665943+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=63896.0
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +27.62% | $1,191,608.37 |
| ESPORTS/USDT:USDT | +27.54% | $9,319,107.11 |
| AKE/USDT:USDT | +17.40% | $48,964,818.72 |
| XEC/USDT:USDT | +7.67% | $3,355,516.25 |
| CRO/USDT:USDT | +7.31% | $2,105,842.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +1.20% | +1.29% |
| USOIL/USDT:USDT | below_1h_threshold | +0.67% | +0.76% |
| CRO/USDT:USDT | below_1h_threshold | +0.64% | +0.73% |
| XEC/USDT:USDT | below_1h_threshold | +0.64% | +0.72% |
| AKE/USDT:USDT | below_1h_threshold | +0.58% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
