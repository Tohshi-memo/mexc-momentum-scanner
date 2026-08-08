# Decision Report

- generated_at: 2026-08-08T01:06:19.822683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10780**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=10780, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +4.08% | **+1.84%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.94% | **+1.07%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.19% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3541件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.93** / 初期 $100.00 (+43.93%)
- 確定: 1496件 (Win 422 / Loss 354 / Flat 720) / skip 2695件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0599 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1070件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T01:06:12.116851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64881.3
- Funnel: target 961 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +94.13% | $3,999,648.20 |
| BLESS/USDT:USDT | +30.86% | $78,999,065.02 |
| HEI/USDT:USDT | +20.20% | $20,383,947.70 |
| SLX/USDT:USDT | +19.79% | $1,701,310.49 |
| EPIC/USDT:USDT | +15.70% | $2,354,996.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +2.29% | +2.30% |
| TUT/USDT:USDT | below_1h_threshold | +2.22% | +2.24% |
| KGEN/USDT:USDT | below_1h_threshold | +1.83% | +1.85% |
| CYS/USDT:USDT | below_1h_threshold | +1.76% | +1.78% |
| CAP/USDT:USDT | below_1h_threshold | +0.54% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
