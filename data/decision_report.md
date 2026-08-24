# Decision Report

- generated_at: 2026-08-24T18:21:31.210555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12533, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.17% | **+1.11%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.01% | **+0.90%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$699.30** / 初期 $100.00 (+599.30%)
- 確定: 4518件 (Win 1378 / Loss 1479 / Flat 1661) / skip 4576件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $699.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3971件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.44** / 初期 $100.00 (+15.44%)
- 確定: 1909件 (Win 560 / Loss 725 / Flat 624) / pending 4件 / skip 2096件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000023 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.44

## 6. Latest Market Context

- 更新: 2026-08-24T18:21:21.786248+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=78990.4
- Funnel: target 1022 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +58.99% | $1,407,182.82 |
| STORJ/USDT:USDT | +10.50% | $3,802,132.44 |
| PONS/USDT:USDT | +9.24% | $1,786,152.52 |
| TUT/USDT:USDT | +6.94% | $62,414,621.69 |
| SCRT/USDT:USDT | +3.99% | $1,096,671.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +3.09% | +2.75% |
| STORJ/USDT:USDT | below_1h_threshold | +2.52% | +2.18% |
| BEAT/USDT:USDT | below_1h_threshold | +2.06% | +1.72% |
| INJ/USDT:USDT | below_1h_threshold | +1.72% | +1.38% |
| TAO/USDT:USDT | below_1h_threshold | +1.42% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
