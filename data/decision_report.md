# Decision Report

- generated_at: 2026-10-30T18:56:24.685321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17862**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=17862, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.74% | **+0.70%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +2.82% | **+2.68%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.62% | **+1.38%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6806件 (Win 1975 / Loss 2181 / Flat 2650) / skip 7617件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.50** / 初期 $100.00 (+263.50%)
- 確定: 4364件 (Win 1173 / Loss 983 / Flat 2208) / skip 6909件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0311 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $363.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6024件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T18:56:14.401552+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=76690.2
- Funnel: target 1090 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +21.86% | $10,100,705.08 |
| AIN/USDT:USDT | +6.16% | $4,601,529.25 |
| PARTI/USDT:USDT | +5.17% | $9,305,703.14 |
| SOXS/USDT:USDT | +4.60% | $51,485,511.94 |
| SQQQ/USDT:USDT | +3.53% | $1,180,086.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PARTI/USDT:USDT | below_1h_threshold | +2.81% | +3.41% |
| BTW/USDT:USDT | below_1h_threshold | +1.92% | +2.52% |
| SOXS/USDT:USDT | below_1h_threshold | +1.39% | +1.99% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.15% | +1.74% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +0.76% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
