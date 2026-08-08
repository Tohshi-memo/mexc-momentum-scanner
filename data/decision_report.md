# Decision Report

- generated_at: 2026-08-08T04:21:10.231811+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10808**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=10808, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.51% | **+0.48%** |
| LIMIT_10PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_9PCT | 7/20 | 35.0% | +0.66% | **+0.23%** |
| LIMIT_8PCT | 8/20 | 40.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 11/20 | 55.0% | +4.45% | **+2.44%** |
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +5.90% | **+2.36%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +3.04% | **+1.82%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +2.20% | **+1.54%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +2.15% | **+1.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$615.31** / 初期 $100.00 (+515.31%)
- 確定: 3809件 (Win 1208 / Loss 1252 / Flat 1349) / skip 3560件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.28% 残高後 $615.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2709件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0995 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1096件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T04:21:03.051527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64951.1
- Funnel: target 961 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +270.31% | $5,867,899.84 |
| BLESS/USDT:USDT | +23.47% | $94,668,052.22 |
| MMT/USDT:USDT | +20.48% | $1,472,166.52 |
| TUT/USDT:USDT | +15.79% | $2,410,182.52 |
| SLX/USDT:USDT | +14.94% | $2,656,193.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +3.81% | +3.88% |
| UB/USDT:USDT | below_1h_threshold | +3.16% | +3.24% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.57% | +2.65% |
| BEAT/USDT:USDT | below_1h_threshold | +2.35% | +2.43% |
| EPIC/USDT:USDT | below_1h_threshold | +1.96% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
