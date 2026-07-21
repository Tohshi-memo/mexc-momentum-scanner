# Decision Report

- generated_at: 2026-07-21T02:01:15.401115+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=9137, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.76% | **+1.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.05% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.21% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.43% | **+0.39%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.33% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$400.40** / 初期 $100.00 (+300.40%)
- 確定: 3199件 (Win 1000 / Loss 1018 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $400.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.85** / 初期 $100.00 (+26.85%)
- 確定: 1098件 (Win 286 / Loss 226 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000217 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1048 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定: 334件 (Win 118 / Loss 147 / Flat 69) / pending 5件 / skip 272件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.45

## 6. Latest Market Context

- 更新: 2026-07-21T02:01:06.431450+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65219.8
- Funnel: target 885 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +32.03% | $2,760,315.77 |
| HEMI/USDT:USDT | +15.07% | $3,123,413.56 |
| BLESS/USDT:USDT | +11.18% | $1,606,579.02 |
| ON/USDT:USDT | +10.56% | $1,928,915.91 |
| LDO/USDT:USDT | +9.23% | $6,082,370.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.91% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.69% | +0.67% |
| ONDO/USDT:USDT | below_1h_threshold | +0.64% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
