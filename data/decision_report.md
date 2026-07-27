# Decision Report

- generated_at: 2026-07-27T23:41:16.842200+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9658**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9658, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.89% | **-1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.64% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.30% | **+0.92%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.06% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$105.86** / 初期 $100.00 (+5.86%)
- 確定トレード: 147件 (TP 50 / SL 92 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.86
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3435件 (Win 1088 / Loss 1118 / Flat 1229) / skip 2784件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1845件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0063 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定: 678件 (Win 221 / Loss 257 / Flat 200) / pending 2件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.60

## 6. Latest Market Context

- 更新: 2026-07-27T23:41:09.848058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63722.7
- Funnel: target 902 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +47.20% | $6,615,849.56 |
| JIMOTHY/USDT:USDT | +17.38% | $1,762,594.09 |
| SOONNETWORK/USDT:USDT | +12.63% | $1,255,872.62 |
| AEON1/USDT:USDT | +11.95% | $1,856,526.20 |
| KAITO/USDT:USDT | +6.62% | $8,491,846.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +1.93% | +1.98% |
| O/USDT:USDT | below_1h_threshold | +1.53% | +1.59% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.36% | +1.41% |
| VVV/USDT:USDT | below_1h_threshold | +1.11% | +1.16% |
| BANK/USDT:USDT | below_1h_threshold | +0.71% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
