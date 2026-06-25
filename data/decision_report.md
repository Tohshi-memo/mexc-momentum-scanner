# Decision Report

- generated_at: 2026-06-25T00:13:49.822278+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7509**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7509, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.74% | **-2.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.21% | **+0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.19% | **-0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.14% | **-0.21%** |
| LIMIT_FIB1272 | 15/20 | 75.0% | -0.71% | **-0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.94% | **+2.94%** |
| ASK_LONG | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.60% | **+2.53%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +3.64% | **+2.36%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +4.38% | **+1.97%** |

## 2. $100 Live Portfolio

- 残高: **$102.43** / 初期 $100.00 (+2.43%)
- 確定トレード: 37件 (TP 14 / SL 23 / EXP 0)
- 最新: KORU/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1949件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 571件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T00:13:42.885025+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=61105.1
- Funnel: target 808 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +21.65% | $10,108,778.19 |
| O/USDT:USDT | +19.70% | $10,481,301.23 |
| KORU/USDT:USDT | +19.63% | $5,339,474.77 |
| MUSTOCK/USDT:USDT | +16.13% | $96,321,123.53 |
| CLO/USDT:USDT | +13.91% | $3,100,317.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +4.64% | +4.55% |
| JUP/USDT:USDT | below_1h_threshold | +1.65% | +1.56% |
| SLX/USDT:USDT | below_1h_threshold | +1.60% | +1.52% |
| ETC/USDT:USDT | below_1h_threshold | +1.33% | +1.24% |
| ICP/USDT:USDT | below_1h_threshold | +1.14% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
