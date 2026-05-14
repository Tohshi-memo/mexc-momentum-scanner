# Decision Report

- generated_at: 2026-05-14T15:02:41.460082+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4300**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4300, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.42% | **+1.14%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.61** / 初期 $100.00 (+19.61%)
- 確定: 355件 (Win 95 / Loss 127 / Flat 133) / skip 506件
- 成長率目線: 平均log +0.000504 / 幾何平均 +0.050% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.61

## 4. Latest Market Context

- 更新: 2026-05-14T15:02:38.456861+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81092.8
- Funnel: target 763 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +72.34% | $12,379,591.34 |
| PLAY/USDT:USDT | +31.57% | $3,253,870.91 |
| GIGA/USDT:USDT | +31.36% | $1,106,165.93 |
| UP/USDT:USDT | +29.65% | $1,724,053.39 |
| TROLLSOL/USDT:USDT | +25.97% | $2,242,224.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +1.53% | +1.32% |
| PLAY/USDT:USDT | below_1h_threshold | +1.11% | +0.90% |
| UB/USDT:USDT | below_1h_threshold | +1.03% | +0.83% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.89% | +0.68% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
