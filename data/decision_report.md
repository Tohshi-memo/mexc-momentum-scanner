# Decision Report

- generated_at: 2026-07-14T03:06:08.658560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8660**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8660, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.96% | **+0.63%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.71% | **+0.45%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.27%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.46% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$102.20** / 初期 $100.00 (+2.20%)
- 確定トレード: 95件 (TP 32 / SL 61 / EXP 2)
- 最新: O/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.03** / 初期 $100.00 (+230.03%)
- 確定: 2828件 (Win 888 / Loss 923 / Flat 1017) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $330.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 660件 (Win 157 / Loss 159 / Flat 344) / skip 1411件
- 成長率目線: 平均log +0.000081 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0195 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.13** / 初期 $100.00 (-0.87%)
- 確定: 41件 (Win 14 / Loss 27 / Flat 0) / pending 1件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIOT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.13

## 6. Latest Market Context

- 更新: 2026-07-14T03:06:02.519673+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62501.1
- Funnel: target 867 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +43.43% | $6,427,392.35 |
| EVAA/USDT:USDT | +20.06% | $21,928,787.92 |
| ZBT/USDT:USDT | +15.24% | $2,012,009.90 |
| VELVET/USDT:USDT | +13.74% | $31,361,562.25 |
| BLAST/USDT:USDT | +13.44% | $1,643,594.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +2.58% | +2.60% |
| VELVET/USDT:USDT | below_1h_threshold | +1.76% | +1.79% |
| EGLD/USDT:USDT | below_1h_threshold | +0.59% | +0.62% |
| T/USDT:USDT | below_1h_threshold | +0.42% | +0.45% |
| LDO/USDT:USDT | below_1h_threshold | +0.39% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
