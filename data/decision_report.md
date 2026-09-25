# Decision Report

- generated_at: 2026-09-25T22:31:25.295747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15544**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15544, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.72% | **-1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.58% | **+0.41%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.32% | **+0.22%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.45% | **-0.09%** |
| LIMIT_BB3S | 7/14 | 50.0% | -1.30% | **-0.65%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.81% | **-0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.55% | **+1.79%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.23% | **+1.77%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.68% | **+1.74%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.33% | **+1.50%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.24% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,210.58** / 初期 $100.00 (+1110.58%)
- 確定: 5908件 (Win 1743 / Loss 1893 / Flat 2272) / skip 6197件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,210.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3477件 (Win 953 / Loss 793 / Flat 1731) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0317 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.01** / 初期 $100.00 (+20.01%)
- 確定: 3174件 (Win 934 / Loss 1256 / Flat 984) / pending 3件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.01

## 6. Latest Market Context

- 更新: 2026-09-25T22:31:13.968034+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=83873.8
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +26.83% | $21,675,470.77 |
| BR/USDT:USDT | +17.15% | $9,234,826.32 |
| SEI/USDT:USDT | +11.44% | $33,309,339.20 |
| SUI/USDT:USDT | +8.48% | $264,274,519.43 |
| BP/USDT:USDT | +7.45% | $1,273,457.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +4.09% | +3.94% |
| SUI/USDT:USDT | below_1h_threshold | +3.24% | +3.09% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.78% | +2.63% |
| PENGU/USDT:USDT | below_1h_threshold | +2.76% | +2.61% |
| LTC/USDT:USDT | below_1h_threshold | +2.68% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
