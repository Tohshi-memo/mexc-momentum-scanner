# Decision Report

- generated_at: 2026-07-21T16:01:21.814060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9192**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=9192, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.54% | **+1.39%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.80% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.08% | **+0.94%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.32% | **+0.29%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.65% | **+0.26%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2504件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.67** / 初期 $100.00 (+32.67%)
- 確定: 1153件 (Win 312 / Loss 249 / Flat 592) / skip 1450件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0520 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $132.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.16** / 初期 $100.00 (+1.16%)
- 確定: 348件 (Win 122 / Loss 154 / Flat 72) / pending 2件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.16

## 6. Latest Market Context

- 更新: 2026-07-21T16:01:12.790307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=66646.3
- Funnel: target 885 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +1.68% | $5,144,067.18 |
| DEXE/USDT:USDT | +1.23% | $12,466,714.49 |
| ESPORTS/USDT:USDT | +1.21% | $9,168,192.95 |
| BULLA/USDT:USDT | +0.87% | $1,409,181.09 |
| CRCLSTOCK/USDT:USDT | +0.35% | $7,252,317.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.08% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.91% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.84% | +1.85% |
| COINBASE/USDT:USDT | below_1h_threshold | +1.40% | +1.40% |
| KORU/USDT:USDT | below_1h_threshold | +1.04% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
