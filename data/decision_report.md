# Decision Report

- generated_at: 2026-09-07T12:36:15.823154+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13882**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13882, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.82% | **-1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.51% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.63** / 初期 $100.00 (+757.63%)
- 確定: 5155件 (Win 1542 / Loss 1681 / Flat 1932) / skip 5288件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUMPFUN/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $857.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4722件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0915 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.02** / 初期 $100.00 (+20.02%)
- 確定: 2473件 (Win 732 / Loss 936 / Flat 805) / pending 2件 / skip 2876件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000308 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $120.02

## 6. Latest Market Context

- 更新: 2026-09-07T12:36:05.730796+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79473.7
- Funnel: target 1063 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +253.82% | $3,768,161.16 |
| BONER/USDT:USDT | +119.91% | $5,977,804.11 |
| DOOD/USDT:USDT | +27.67% | $1,243,192.28 |
| IOST/USDT:USDT | +25.04% | $1,262,526.30 |
| AKE/USDT:USDT | +21.84% | $10,314,763.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +2.78% | +2.66% |
| CAKE/USDT:USDT | below_1h_threshold | +2.72% | +2.60% |
| SUI/USDT:USDT | below_1h_threshold | +2.62% | +2.50% |
| XLM/USDT:USDT | below_1h_threshold | +2.03% | +1.91% |
| KAS/USDT:USDT | below_1h_threshold | +1.96% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
