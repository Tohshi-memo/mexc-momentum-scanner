# Decision Report

- generated_at: 2026-08-24T19:16:29.069349+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12542**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12542, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +6.18% | **+1.55%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +4.67% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$695.71** / 初期 $100.00 (+595.71%)
- 確定: 4526件 (Win 1381 / Loss 1484 / Flat 1661) / skip 4577件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $695.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3980件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.84** / 初期 $100.00 (+15.84%)
- 確定: 1910件 (Win 561 / Loss 725 / Flat 624) / pending 3件 / skip 2107件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000061 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.84

## 6. Latest Market Context

- 更新: 2026-08-24T19:16:18.126145+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78995.9
- Funnel: target 1022 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +75.09% | $2,180,292.63 |
| STORJ/USDT:USDT | +10.21% | $3,892,375.38 |
| CASHCAT/USDT:USDT | +7.58% | $2,091,324.39 |
| TUT/USDT:USDT | +7.33% | $62,455,589.17 |
| MONAD/USDT:USDT | +7.20% | $3,049,766.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +2.90% | +2.78% |
| CYS/USDT:USDT | below_1h_threshold | +2.89% | +2.77% |
| FF/USDT:USDT | below_1h_threshold | +2.79% | +2.67% |
| KORU/USDT:USDT | below_1h_threshold | +2.32% | +2.19% |
| SOXL/USDT:USDT | below_1h_threshold | +1.53% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
