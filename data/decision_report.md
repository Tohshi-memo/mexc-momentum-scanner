# Decision Report

- generated_at: 2026-08-27T00:11:17.656494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12759**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=12759, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.51% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.55% | **+1.48%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.98% | **+0.78%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.60% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$734.20** / 初期 $100.00 (+634.20%)
- 確定: 4656件 (Win 1414 / Loss 1527 / Flat 1715) / skip 4664件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $734.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4169件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1362 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1982件 (Win 580 / Loss 758 / Flat 644) / pending 0件 / skip 2250件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T00:11:10.343358+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=78877.4
- Funnel: target 1023 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +23.11% | $1,684,897.26 |
| ONG/USDT:USDT | +22.82% | $42,057,885.06 |
| VET/USDT:USDT | +20.47% | $2,447,266.50 |
| ONT/USDT:USDT | +20.26% | $4,919,089.69 |
| SPX/USDT:USDT | +13.54% | $4,814,141.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONT/USDT:USDT | below_1h_threshold | +1.62% | +1.76% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.57% | +1.71% |
| VET/USDT:USDT | below_1h_threshold | +1.10% | +1.25% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.00% | +1.15% |
| SOXL/USDT:USDT | below_1h_threshold | +0.95% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
