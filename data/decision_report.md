# Decision Report

- generated_at: 2026-08-13T02:06:31.195428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11417**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11417, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +7.96% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.04% | **+0.71%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.91% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.98% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.87% | **+2.32%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.18% | **+2.07%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.65% | **+2.01%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4028件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$148.27** / 初期 $100.00 (+48.27%)
- 確定: 1605件 (Win 453 / Loss 376 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1223 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $148.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.50** / 初期 $100.00 (+15.50%)
- 確定: 1425件 (Win 418 / Loss 536 / Flat 471) / pending 4件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000138 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $115.50

## 6. Latest Market Context

- 更新: 2026-08-13T02:06:22.955145+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63415.6
- Funnel: target 972 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +36.99% | $7,554,050.73 |
| APR/USDT:USDT | +34.85% | $13,342,935.36 |
| BTW/USDT:USDT | +17.31% | $22,291,845.70 |
| BANK/USDT:USDT | +14.68% | $3,262,241.40 |
| COOKIE/USDT:USDT | +11.56% | $1,013,796.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +3.02% | +3.04% |
| BANK/USDT:USDT | below_1h_threshold | +2.76% | +2.78% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.16% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.14% |
| COTI/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
