# Decision Report

- generated_at: 2026-09-02T00:06:29.533931+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13280**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13280, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +3.24% | **+1.46%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.36% | **+2.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.00% | **+1.90%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.76%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.75% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$832.57** / 初期 $100.00 (+732.57%)
- 確定: 4915件 (Win 1498 / Loss 1616 / Flat 1801) / skip 4926件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $832.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.92** / 初期 $100.00 (+75.92%)
- 確定: 2259件 (Win 632 / Loss 542 / Flat 1085) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0938 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2662件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T00:06:19.813978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77425.0
- Funnel: target 1036 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +25.61% | $1,295,236.32 |
| UAI/USDT:USDT | +23.79% | $15,735,261.47 |
| BONER/USDT:USDT | +19.35% | $2,296,469.55 |
| MAGMA/USDT:USDT | +19.09% | $3,830,098.53 |
| ACE/USDT:USDT | +14.50% | $9,052,402.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_1h_threshold | +4.71% | +4.68% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.62% | +1.58% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.48% |
| TRIA/USDT:USDT | below_1h_threshold | +1.32% | +1.29% |
| USELESS/USDT:USDT | below_1h_threshold | +0.83% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
