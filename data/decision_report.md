# Decision Report

- generated_at: 2026-08-12T11:01:35.091202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11363**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11363, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.65% | **+0.66%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.50% | **+0.42%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.55% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 181件 (TP 70 / SL 106 / EXP 5)
- 最新: ACE/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3948件 (Win 1232 / Loss 1291 / Flat 1425) / skip 3976件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.30** / 初期 $100.00 (+47.30%)
- 確定: 1596件 (Win 449 / Loss 374 / Flat 773) / skip 3178件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0413 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.31** / 初期 $100.00 (+14.31%)
- 確定: 1377件 (Win 413 / Loss 534 / Flat 430) / pending 4件 / skip 1453件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $114.31

## 6. Latest Market Context

- 更新: 2026-08-12T11:01:25.420007+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=64179.9
- Funnel: target 967 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +82.89% | $3,906,340.25 |
| BR/USDT:USDT | +68.26% | $3,948,154.87 |
| PROM/USDT:USDT | +60.80% | $8,978,124.72 |
| JIMOTHY/USDT:USDT | +55.66% | $2,785,113.73 |
| BEAT/USDT:USDT | +32.51% | $88,777,439.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.38% | +2.28% |
| BR/USDT:USDT | below_1h_threshold | +0.90% | +0.79% |
| ACE/USDT:USDT | below_1h_threshold | +0.83% | +0.73% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.55% |
| BEAT/USDT:USDT | below_1h_threshold | +0.62% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
