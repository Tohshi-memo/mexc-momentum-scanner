# Decision Report

- generated_at: 2026-08-24T17:21:31.151920+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12529, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.02% | **-1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +2.88% | **+0.90%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.37% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.34% | **+1.14%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.01% | **+0.90%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.14% | **+0.75%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.64% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.34** / 初期 $100.00 (+606.34%)
- 確定: 4514件 (Win 1378 / Loss 1477 / Flat 1659) / skip 4576件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $706.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3968件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.44** / 初期 $100.00 (+15.44%)
- 確定: 1909件 (Win 560 / Loss 725 / Flat 624) / pending 4件 / skip 2091件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000080 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.44

## 6. Latest Market Context

- 更新: 2026-08-24T17:21:22.011423+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=78837.7
- Funnel: target 1022 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +23.52% | $3,308,158.29 |
| TUT/USDT:USDT | +8.73% | $61,952,274.17 |
| SCRT/USDT:USDT | +7.75% | $1,089,905.41 |
| CATE/USDT:USDT | +5.39% | $1,247,265.30 |
| INJ/USDT:USDT | +4.16% | $16,852,636.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +1.92% | +2.15% |
| BTW/USDT:USDT | below_1h_threshold | +1.79% | +2.02% |
| PONS/USDT:USDT | below_1h_threshold | +1.62% | +1.85% |
| CATE/USDT:USDT | below_1h_threshold | +1.48% | +1.71% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
