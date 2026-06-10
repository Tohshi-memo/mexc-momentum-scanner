# Decision Report

- generated_at: 2026-06-10T00:44:10.219335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6170**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6170, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.95% | **+0.50%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.68% | **+0.38%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.59% | **+0.33%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.27** / 初期 $100.00 (+47.27%)
- 確定: 1189件 (Win 297 / Loss 375 / Flat 517) / skip 1542件
- 成長率目線: 平均log +0.000326 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_5PCT_LONG` SL_HIT account -0.50% 残高後 $147.27

## 4. Latest Market Context

- 更新: 2026-06-10T00:44:07.668691+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=61457.0
- Funnel: target 778 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +42.00% | $11,033,604.20 |
| H/USDT:USDT | +22.48% | $52,499,271.31 |
| STG/USDT:USDT | +21.40% | $2,866,861.98 |
| HOME/USDT:USDT | +15.09% | $4,484,661.01 |
| OPN/USDT:USDT | +12.83% | $2,044,658.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_1h_threshold | +4.59% | +4.97% |
| BTW/USDT:USDT | below_1h_threshold | +3.87% | +4.25% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.89% | +3.28% |
| UB/USDT:USDT | below_1h_threshold | +2.26% | +2.64% |
| H/USDT:USDT | below_1h_threshold | +1.68% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
