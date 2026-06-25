# Decision Report

- generated_at: 2026-06-25T04:30:46.585784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7521**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7521, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.03% | **+0.00%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.51% | **-0.25%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.52% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.23% | **+1.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.87% | **+0.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.31% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.80** / 初期 $100.00 (+124.80%)
- 確定: 2124件 (Win 629 / Loss 710 / Flat 785) / skip 1958件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $224.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 582件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T04:30:35.200685+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=60860.0
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +22.72% | $12,444,196.04 |
| KORU/USDT:USDT | +17.40% | $5,691,166.91 |
| MUSTOCK/USDT:USDT | +16.89% | $101,927,685.02 |
| MAVIA/USDT:USDT | +13.98% | $1,538,450.60 |
| RESOLV/USDT:USDT | +13.71% | $2,665,506.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.90% | +3.89% |
| RESOLV/USDT:USDT | below_1h_threshold | +3.07% | +3.06% |
| SYN/USDT:USDT | below_1h_threshold | +2.65% | +2.64% |
| MMT/USDT:USDT | below_1h_threshold | +2.12% | +2.11% |
| ID/USDT:USDT | below_1h_threshold | +1.99% | +1.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
