# Decision Report

- generated_at: 2026-06-24T03:54:27.515039+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7457**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7457, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.23% | **+0.22%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| ASK | 20/20 | 100.0% | -0.07% | **-0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -2.00% | **-0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.21% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.38** / 初期 $100.00 (+131.38%)
- 確定: 2088件 (Win 620 / Loss 693 / Flat 775) / skip 1930件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1618_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KORU/USDT:USDT `LIMIT_FIB1618_LONG` EXPIRED account -0.35% 残高後 $231.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 540件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T03:44:07.205017+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=62779.9
- Funnel: target 802 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +45.30% | $11,193,386.47 |
| CLO/USDT:USDT | +25.49% | $5,461,708.75 |
| BEAT/USDT:USDT | +18.10% | $68,706,129.18 |
| ID/USDT:USDT | +13.63% | $1,646,175.92 |
| SYN/USDT:USDT | +12.96% | $15,162,743.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.07% | +2.78% |
| ID/USDT:USDT | below_1h_threshold | +2.85% | +2.55% |
| MVLL/USDT:USDT | below_1h_threshold | +2.01% | +1.72% |
| UP/USDT:USDT | below_1h_threshold | +1.64% | +1.35% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +1.22% | +0.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
