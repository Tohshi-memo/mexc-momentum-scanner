# Decision Report

- generated_at: 2026-10-29T11:31:14.537359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17769**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=17769, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +2.62% | **+1.44%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.48% | **-0.24%** |
| MARKET_LONG | 20/20 | 100.0% | -0.32% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6803件 (Win 1975 / Loss 2180 / Flat 2648) / skip 7527件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.47** / 初期 $100.00 (+264.47%)
- 確定: 4290件 (Win 1161 / Loss 975 / Flat 2154) / skip 6890件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0040 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.04% 残高後 $364.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5931件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T11:31:04.150554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80110.6
- Funnel: target 1084 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +61.48% | $3,961,486.71 |
| BEAT/USDT:USDT | +23.74% | $11,472,961.98 |
| INIT/USDT:USDT | +18.49% | $2,546,744.77 |
| APR/USDT:USDT | +14.71% | $2,384,196.49 |
| BULLA/USDT:USDT | +11.09% | $1,778,578.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +4.56% | +4.75% |
| COHRSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +3.06% |
| APR/USDT:USDT | below_1h_threshold | +2.04% | +2.22% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.71% |
| UAI/USDT:USDT | below_1h_threshold | +1.36% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
