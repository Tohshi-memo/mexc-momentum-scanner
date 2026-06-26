# Decision Report

- generated_at: 2026-06-26T09:51:35.358433+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7621**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7621, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.21% | **+0.17%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.71% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.20% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.93** / 初期 $100.00 (+120.93%)
- 確定: 2147件 (Win 631 / Loss 715 / Flat 801) / skip 2035件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $220.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 650件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T09:51:27.629429+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=59846.7
- Funnel: target 810 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +40.93% | $1,523,812.80 |
| MAGMA/USDT:USDT | +35.41% | $1,373,087.82 |
| G/USDT:USDT | +32.68% | $10,075,410.52 |
| UB/USDT:USDT | +32.31% | $1,844,786.03 |
| AIN/USDT:USDT | +31.78% | $5,954,049.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +2.26% | +2.87% |
| W/USDT:USDT | below_1h_threshold | +2.05% | +2.66% |
| VELVET/USDT:USDT | below_1h_threshold | +1.84% | +2.45% |
| BILL/USDT:USDT | below_1h_threshold | +1.68% | +2.29% |
| AIN/USDT:USDT | below_1h_threshold | +1.56% | +2.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
