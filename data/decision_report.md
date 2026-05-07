# Decision Report

- generated_at: 2026-05-07T16:32:59.084523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3660**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3660, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.81%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.74% | **+0.59%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.33% | **+1.51%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.83% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 154件 (Win 46 / Loss 53 / Flat 55) / skip 67件
- 成長率目線: 平均log +0.000745 / 幾何平均 +0.075% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:32:55.132962+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79961.3
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +32.57% | $4,439,406.97 |
| HIGH/USDT:USDT | +13.31% | $1,084,071.40 |
| LAB/USDT:USDT | +9.83% | $268,689,403.56 |
| FHE/USDT:USDT | +8.05% | $14,049,296.35 |
| BILL/USDT:USDT | +4.88% | $11,697,024.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.88% | +4.76% |
| DYDX/USDT:USDT | below_1h_threshold | +3.90% | +3.77% |
| NOT/USDT:USDT | below_1h_threshold | +3.33% | +3.21% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.30% | +3.17% |
| AVNT/USDT:USDT | below_1h_threshold | +3.18% | +3.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
