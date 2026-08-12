# Decision Report

- generated_at: 2026-08-12T12:01:18.987708+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11367**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11367, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.09% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.74% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 181件 (TP 70 / SL 106 / EXP 5)
- 最新: ACE/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3948件 (Win 1232 / Loss 1291 / Flat 1425) / skip 3980件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.30** / 初期 $100.00 (+47.30%)
- 確定: 1596件 (Win 449 / Loss 374 / Flat 773) / skip 3182件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0458 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.61** / 初期 $100.00 (+14.61%)
- 確定: 1381件 (Win 414 / Loss 534 / Flat 433) / pending 3件 / skip 1454件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $114.61

## 6. Latest Market Context

- 更新: 2026-08-12T12:01:09.480213+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64220.0
- Funnel: target 967 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +87.86% | $4,415,534.50 |
| PROM/USDT:USDT | +67.88% | $9,760,492.70 |
| BR/USDT:USDT | +60.95% | $4,915,516.99 |
| JIMOTHY/USDT:USDT | +56.75% | $2,832,562.04 |
| BEAT/USDT:USDT | +32.61% | $88,822,056.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.85% | +3.83% |
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.45% |
| SOXL/USDT:USDT | below_1h_threshold | +1.22% | +1.20% |
| SNXX/USDT:USDT | below_1h_threshold | +0.93% | +0.91% |
| LITESTOCK/USDT:USDT | below_1h_threshold | +0.86% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
