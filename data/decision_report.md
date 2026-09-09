# Decision Report

- generated_at: 2026-09-09T18:06:12.982140+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14099**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14099, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.86% | **-1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.64% | **+2.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.41% | **+2.38%** |
| MARKET_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.77% | **+1.44%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +5.47% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5347件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.21** / 初期 $100.00 (+92.21%)
- 確定: 2693件 (Win 739 / Loss 630 / Flat 1324) / skip 4817件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0531 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $192.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 2620件 (Win 765 / Loss 1001 / Flat 854) / pending 0件 / skip 2958件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account -0.09% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-09-09T18:06:04.990788+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78738.9
- Funnel: target 1064 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOCK/USDT:USDT | +25.11% | $1,517,706.02 |
| IOST/USDT:USDT | +11.41% | $20,660,537.31 |
| CATE/USDT:USDT | +11.00% | $2,062,916.48 |
| BULLA/USDT:USDT | +8.97% | $2,914,640.97 |
| OL/USDT:USDT | +7.38% | $2,692,604.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +2.65% | +2.64% |
| BULLA/USDT:USDT | below_1h_threshold | +2.60% | +2.60% |
| CATE/USDT:USDT | below_1h_threshold | +2.41% | +2.41% |
| CNPY/USDT:USDT | below_1h_threshold | +1.87% | +1.87% |
| SOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
