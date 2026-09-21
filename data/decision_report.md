# Decision Report

- generated_at: 2026-09-21T23:41:19.361258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15282**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15282, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.30% | **+0.29%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.38% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.63% | **+0.13%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.07% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.34%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.44% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,180.81** / 初期 $100.00 (+1080.81%)
- 確定: 5773件 (Win 1717 / Loss 1855 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,180.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.65** / 初期 $100.00 (+149.65%)
- 確定: 3322件 (Win 918 / Loss 767 / Flat 1637) / skip 5371件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0592 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.99** / 初期 $100.00 (+22.99%)
- 確定: 3055件 (Win 898 / Loss 1194 / Flat 963) / pending 4件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.99

## 6. Latest Market Context

- 更新: 2026-09-21T23:41:08.197668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=86464.4
- Funnel: target 1055 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +29.43% | $8,481,030.10 |
| ALCH/USDT:USDT | +26.06% | $2,093,199.48 |
| PTB/USDT:USDT | +14.99% | $1,204,091.77 |
| 4STOCK/USDT:USDT | +14.40% | $1,030,402.08 |
| EVAA/USDT:USDT | +14.07% | $1,955,964.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.82% | +3.77% |
| SAGA/USDT:USDT | below_1h_threshold | +1.63% | +1.58% |
| EGLD/USDT:USDT | below_1h_threshold | +1.50% | +1.45% |
| APT/USDT:USDT | below_1h_threshold | +1.39% | +1.34% |
| AERO/USDT:USDT | below_1h_threshold | +1.33% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
