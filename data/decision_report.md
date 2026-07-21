# Decision Report

- generated_at: 2026-07-21T03:46:14.286023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9149**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=9149, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.97% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.41% | **+1.27%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.11% | **+0.89%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.89% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定トレード: 125件 (TP 44 / SL 76 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT SL_HIT PnL -3.51% 残高後 $108.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.88** / 初期 $100.00 (+319.88%)
- 確定: 3211件 (Win 1007 / Loss 1021 / Flat 1183) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KIOXIASTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.65% 残高後 $419.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 1110件 (Win 293 / Loss 229 / Flat 588) / skip 1450件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1210 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.44% 残高後 $131.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.08** / 初期 $100.00 (+1.08%)
- 確定: 340件 (Win 120 / Loss 151 / Flat 69) / pending 1件 / skip 281件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.08

## 6. Latest Market Context

- 更新: 2026-07-21T03:46:06.462042+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=65470.8
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +66.21% | $2,754,606.11 |
| JIMOTHY/USDT:USDT | +28.00% | $2,863,058.95 |
| ZHIPUSTOCK/USDT:USDT | +23.31% | $1,545,224.81 |
| BLESS/USDT:USDT | +13.52% | $2,161,731.47 |
| ON/USDT:USDT | +13.07% | $2,132,413.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +3.52% | +3.39% |
| KORU/USDT:USDT | below_1h_threshold | +2.97% | +2.85% |
| RE/USDT:USDT | below_1h_threshold | +2.97% | +2.84% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.63% | +2.50% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.07% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
