# Decision Report

- generated_at: 2026-11-03T07:26:19.104442+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18063**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=18063, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.14% | **+0.10%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.58% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.82% | **+0.46%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.68% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,505.91** / 初期 $100.00 (+1405.91%)
- 確定: 6915件 (Win 2000 / Loss 2218 / Flat 2697) / skip 7709件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,505.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$380.36** / 初期 $100.00 (+280.36%)
- 確定: 4488件 (Win 1204 / Loss 1001 / Flat 2283) / skip 6986件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0471 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $380.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6223件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T07:26:06.259347+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=76735.7
- Funnel: target 1079 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +36.27% | $16,227,319.48 |
| ICNT/USDT:USDT | +15.54% | $1,450,635.92 |
| JCT/USDT:USDT | +12.46% | $2,825,250.82 |
| UAI/USDT:USDT | +11.45% | $6,871,929.09 |
| SOXS/USDT:USDT | +11.28% | $28,159,970.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOT/USDT:USDT | below_1h_threshold | +2.90% | +2.66% |
| XMR/USDT:USDT | below_1h_threshold | +2.56% | +2.32% |
| BEAT/USDT:USDT | below_1h_threshold | +1.03% | +0.79% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.78% | +0.54% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.61% | +0.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
