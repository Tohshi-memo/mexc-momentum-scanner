# Decision Report

- generated_at: 2026-08-22T00:01:18.360033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12277**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12277, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.19% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.76% | **+2.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.83% | **+2.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.92% | **+1.73%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.59% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$682.34** / 初期 $100.00 (+582.34%)
- 確定: 4397件 (Win 1346 / Loss 1439 / Flat 1612) / skip 4441件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $682.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.27** / 初期 $100.00 (+55.27%)
- 確定: 1883件 (Win 519 / Loss 450 / Flat 914) / skip 3805件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1584 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $155.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.50** / 初期 $100.00 (+17.50%)
- 確定: 1828件 (Win 542 / Loss 694 / Flat 592) / pending 1件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $117.50

## 6. Latest Market Context

- 更新: 2026-08-22T00:01:08.078868+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78261.7
- Funnel: target 1018 → liquid 214 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +254.63% | $3,159,380.95 |
| CATE/USDT:USDT | +64.74% | $11,362,148.00 |
| JIMOTHY/USDT:USDT | +29.65% | $1,624,866.57 |
| AGI/USDT:USDT | +19.61% | $1,588,882.29 |
| MAGMA/USDT:USDT | +16.13% | $2,727,051.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +4.18% | +4.24% |
| ONT/USDT:USDT | below_1h_threshold | +2.09% | +2.15% |
| AGI/USDT:USDT | below_1h_threshold | +0.99% | +1.05% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.52% | +0.58% |
| KAITO/USDT:USDT | below_1h_threshold | +0.51% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
