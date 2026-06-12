# Decision Report

- generated_at: 2026-06-12T08:42:35.277778+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6488**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6488, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +5.02% | **+0.75%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.39% | **+0.37%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.79% | **+0.32%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$161.50** / 初期 $100.00 (+61.50%)
- 確定: 1363件 (Win 368 / Loss 439 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $161.50

## 4. Latest Market Context

- 更新: 2026-06-12T08:42:32.059155+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=63370.6
- Funnel: target 779 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +104.27% | $148,217,861.93 |
| ESPORTS/USDT:USDT | +43.27% | $37,273,437.38 |
| NAORIS/USDT:USDT | +38.50% | $2,844,371.67 |
| XPL/USDT:USDT | +37.74% | $9,173,037.13 |
| STG/USDT:USDT | +25.63% | $14,770,013.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +5.00% | +4.52% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.50% | +4.02% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.95% | +3.47% |
| JUP/USDT:USDT | below_1h_threshold | +2.23% | +1.74% |
| UB/USDT:USDT | below_1h_threshold | +2.03% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
