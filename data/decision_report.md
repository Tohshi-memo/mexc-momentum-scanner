# Decision Report

- generated_at: 2026-08-24T18:36:43.855548+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12536**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12536, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |
| LIMIT_BB3S | 7/13 | 53.8% | -0.69% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.62% | **+1.39%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +5.50% | **+1.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$699.24** / 初期 $100.00 (+599.24%)
- 確定: 4521件 (Win 1379 / Loss 1481 / Flat 1661) / skip 4576件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $699.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3974件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.44** / 初期 $100.00 (+15.44%)
- 確定: 1909件 (Win 560 / Loss 725 / Flat 624) / pending 4件 / skip 2101件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.44

## 6. Latest Market Context

- 更新: 2026-08-24T18:36:29.609894+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=78908.5
- Funnel: target 1022 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1, 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +69.70% | $1,734,571.55 |
| STORJ/USDT:USDT | +13.55% | $3,857,386.03 |
| MONAD/USDT:USDT | +5.85% | $2,703,006.79 |
| XMR/USDT:USDT | +5.68% | $4,818,051.20 |
| TUT/USDT:USDT | +5.65% | $62,673,236.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +4.76% | +4.53% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.19% | +2.96% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.13% | +2.90% |
| BTW/USDT:USDT | below_1h_threshold | +2.68% | +2.45% |
| XMR/USDT:USDT | below_1h_threshold | +2.63% | +2.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
