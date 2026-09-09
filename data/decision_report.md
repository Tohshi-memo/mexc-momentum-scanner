# Decision Report

- generated_at: 2026-09-09T19:01:28.495364+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14109**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14109, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.31% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.30% | **+3.44%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.77% | **+1.44%** |
| LIMIT_ATR_LONG | 5/20 | 25.0% | +4.63% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5357件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$196.51** / 初期 $100.00 (+96.51%)
- 確定: 2703件 (Win 744 / Loss 631 / Flat 1328) / skip 4817件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2326 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $196.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.86** / 初期 $100.00 (+18.86%)
- 確定: 2624件 (Win 768 / Loss 1001 / Flat 855) / pending 6件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000729 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.86

## 6. Latest Market Context

- 更新: 2026-09-09T19:01:18.308365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78415.6
- Funnel: target 1064 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOCK/USDT:USDT | +38.06% | $1,560,476.88 |
| IOST/USDT:USDT | +25.65% | $24,777,813.01 |
| CATE/USDT:USDT | +23.48% | $2,211,361.48 |
| BULLA/USDT:USDT | +11.10% | $3,309,607.29 |
| COTI/USDT:USDT | +10.62% | $1,568,656.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.33% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +1.07% | +1.03% |
| CATE/USDT:USDT | below_1h_threshold | +0.90% | +0.86% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.78% |
| SOXS/USDT:USDT | below_1h_threshold | +0.79% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
