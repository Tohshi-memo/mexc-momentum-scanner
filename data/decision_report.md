# Decision Report

- generated_at: 2026-08-23T00:16:14.603131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12426**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12426, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +5.25% | **+1.31%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +8.00% | **+3.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.69% | **+1.44%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.22** / 初期 $100.00 (+606.22%)
- 確定: 4456件 (Win 1365 / Loss 1456 / Flat 1635) / skip 4531件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $706.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3903件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0090 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2036件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T00:16:06.108092+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77067.7
- Funnel: target 1018 → liquid 208 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +39.89% | $41,694,480.81 |
| CATE/USDT:USDT | +39.63% | $12,454,497.48 |
| UAI/USDT:USDT | +12.64% | $3,012,307.92 |
| ZRO/USDT:USDT | +12.37% | $8,556,487.85 |
| STX/USDT:USDT | +12.14% | $10,063,583.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +2.90% | +2.92% |
| UP/USDT:USDT | below_1h_threshold | +2.82% | +2.84% |
| TUT/USDT:USDT | below_1h_threshold | +1.59% | +1.61% |
| CC/USDT:USDT | below_1h_threshold | +1.52% | +1.54% |
| UAI/USDT:USDT | below_1h_threshold | +1.18% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
