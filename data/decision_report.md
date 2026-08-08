# Decision Report

- generated_at: 2026-08-08T02:46:29.854281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10790**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=10790, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.33% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3551件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.00** / 初期 $100.00 (+43.00%)
- 確定: 1506件 (Win 424 / Loss 358 / Flat 724) / skip 2695件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0461 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $143.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000092 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T02:46:20.964073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64888.1
- Funnel: target 961 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1, 4h RSI 92.9 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +89.02% | $4,344,427.04 |
| BLESS/USDT:USDT | +46.83% | $90,944,316.52 |
| EPIC/USDT:USDT | +19.21% | $2,410,478.95 |
| GWEI/USDT:USDT | +17.91% | $2,077,673.39 |
| BTW/USDT:USDT | +17.59% | $7,121,811.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.41% | +3.39% |
| TUT/USDT:USDT | below_1h_threshold | +2.72% | +2.71% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.66% | +2.65% |
| CAP/USDT:USDT | below_1h_threshold | +2.18% | +2.17% |
| RE/USDT:USDT | below_1h_threshold | +2.15% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
