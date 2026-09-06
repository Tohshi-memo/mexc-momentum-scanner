# Decision Report

- generated_at: 2026-09-06T03:06:24.379352+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13791**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13791, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.88% | **+0.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 5/15 | 33.3% | -0.02% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +4.36% | **+1.75%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.27%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.20% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$871.63** / 初期 $100.00 (+771.63%)
- 確定: 5097件 (Win 1531 / Loss 1662 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $871.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.01** / 初期 $100.00 (+90.01%)
- 確定: 2536件 (Win 707 / Loss 600 / Flat 1229) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0441 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $190.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.30** / 初期 $100.00 (+20.30%)
- 確定: 2408件 (Win 718 / Loss 913 / Flat 777) / pending 4件 / skip 2854件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.30

## 6. Latest Market Context

- 更新: 2026-09-06T03:06:16.646055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79885.2
- Funnel: target 1050 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +42.64% | $8,622,718.46 |
| ARB/USDT:USDT | +42.40% | $111,951,736.06 |
| FLOCK/USDT:USDT | +28.19% | $1,049,334.94 |
| BASECAT/USDT:USDT | +21.61% | $2,059,669.72 |
| SUSHI/USDT:USDT | +20.77% | $4,258,112.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +2.62% | +2.60% |
| SUSHI/USDT:USDT | below_1h_threshold | +0.75% | +0.73% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.47% | +0.46% |
| ENA/USDT:USDT | below_1h_threshold | +0.41% | +0.39% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.37% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
