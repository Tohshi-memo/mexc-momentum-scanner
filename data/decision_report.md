# Decision Report

- generated_at: 2026-08-13T07:51:39.364727+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11430**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=11430, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.25% | **+1.35%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.27% | **+1.01%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.08% | **+0.92%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +1.39% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.62% | **+1.54%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.29% | **+1.49%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.85% | **+1.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4041件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$148.82** / 初期 $100.00 (+48.82%)
- 確定: 1618件 (Win 459 / Loss 383 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1363 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $148.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.79** / 初期 $100.00 (+15.79%)
- 確定: 1438件 (Win 422 / Loss 541 / Flat 475) / pending 5件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.79

## 6. Latest Market Context

- 更新: 2026-08-13T07:51:27.959944+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63824.4
- Funnel: target 972 → liquid 181 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACU/USDT:USDT | +35.03% | $4,136,670.76 |
| BTW/USDT:USDT | +15.45% | $29,207,704.83 |
| COTI/USDT:USDT | +14.30% | $9,591,429.71 |
| APR/USDT:USDT | +11.81% | $16,105,386.63 |
| VELVET/USDT:USDT | +9.84% | $23,833,368.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACU/USDT:USDT | below_1h_threshold | +2.18% | +2.33% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.90% | +2.04% |
| KAITO/USDT:USDT | below_1h_threshold | +1.62% | +1.77% |
| RE/USDT:USDT | below_1h_threshold | +0.75% | +0.89% |
| BILL/USDT:USDT | below_1h_threshold | +0.51% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
