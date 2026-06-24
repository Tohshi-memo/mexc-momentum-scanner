# Decision Report

- generated_at: 2026-06-24T02:41:11.491299+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7456, expectancy=-0.05%
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
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.34% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.20** / 初期 $100.00 (+132.20%)
- 確定: 2087件 (Win 620 / Loss 692 / Flat 775) / skip 1930件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1618_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $232.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 539件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T02:41:06.946082+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=62727.1
- Funnel: target 802 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +48.92% | $10,467,867.10 |
| CLO/USDT:USDT | +23.37% | $5,501,090.09 |
| BEAT/USDT:USDT | +20.63% | $66,693,761.64 |
| SYN/USDT:USDT | +13.34% | $15,346,988.04 |
| DYDX/USDT:USDT | +10.54% | $4,150,027.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +3.29% | +3.58% |
| CLO/USDT:USDT | below_1h_threshold | +2.83% | +3.11% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.28% | +2.56% |
| DYDX/USDT:USDT | below_1h_threshold | +1.88% | +2.16% |
| ID/USDT:USDT | below_1h_threshold | +1.11% | +1.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
