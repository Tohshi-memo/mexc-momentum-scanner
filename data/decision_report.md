# Decision Report

- generated_at: 2026-07-18T07:51:15.838895+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8922**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=8922, expectancy=+0.01%
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
| LIMIT_3PCT | 14/20 | 70.0% | +0.75% | **+0.53%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.55% | **+0.52%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.28% | **+0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.82% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.17% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.41% | **+0.84%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$363.69** / 初期 $100.00 (+263.69%)
- 確定: 3037件 (Win 942 / Loss 966 / Flat 1129) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STAR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $363.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.73** / 初期 $100.00 (+10.73%)
- 確定: 884件 (Win 208 / Loss 180 / Flat 496) / skip 1449件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0113 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STAR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.57** / 初期 $100.00 (-0.43%)
- 確定: 178件 (Win 56 / Loss 95 / Flat 27) / pending 5件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000348 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STAR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.57

## 6. Latest Market Context

- 更新: 2026-07-18T07:51:06.878466+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63982.4
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +51.80% | $55,937,109.72 |
| ESPORTS/USDT:USDT | +33.16% | $14,044,622.20 |
| TRADOOR/USDT:USDT | +29.99% | $2,464,939.71 |
| BSB/USDT:USDT | +11.83% | $1,318,031.71 |
| VVV/USDT:USDT | +11.56% | $2,975,692.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +2.95% | +2.90% |
| LAB/USDT:USDT | below_1h_threshold | +2.71% | +2.67% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| VVV/USDT:USDT | below_1h_threshold | +1.05% | +1.01% |
| XEC/USDT:USDT | below_1h_threshold | +0.93% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
