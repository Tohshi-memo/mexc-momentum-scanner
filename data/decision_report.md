# Decision Report

- generated_at: 2026-11-02T08:46:11.717508+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.82% / filled 20/20。**
- 全期間 MARKET基準: n=18017, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.71% | **+1.62%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.90% | **+1.62%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.82% | **+4.82%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,530.01** / 初期 $100.00 (+1430.01%)
- 確定: 6869件 (Win 1991 / Loss 2203 / Flat 2675) / skip 7709件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,530.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$379.19** / 初期 $100.00 (+279.19%)
- 確定: 4457件 (Win 1194 / Loss 990 / Flat 2273) / skip 6971件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0289 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $379.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T08:46:03.065101+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=78276.2
- Funnel: target 1088 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +32.41% | $15,895,417.08 |
| LYN/USDT:USDT | +28.39% | $2,766,062.21 |
| EVAA/USDT:USDT | +16.20% | $5,675,122.58 |
| KORU/USDT:USDT | +9.79% | $36,152,465.83 |
| SAMSUNGSTOCK/USDT:USDT | +3.89% | $22,680,849.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_1h_threshold | +1.47% | +1.22% |
| DOT/USDT:USDT | below_1h_threshold | +0.62% | +0.37% |
| ETH/USDT:USDT | below_1h_threshold | +0.60% | +0.35% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +0.46% | +0.21% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +0.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
