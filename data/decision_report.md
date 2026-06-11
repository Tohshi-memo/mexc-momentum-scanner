# Decision Report

- generated_at: 2026-06-11T22:43:05.538772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6421**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=6421, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.24% | **+0.56%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.61% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.46% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.85% | **+0.85%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.11% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1655件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-11T22:42:59.560257+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63472.3
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 84.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +85.71% | $18,699,479.03 |
| VELVET/USDT:USDT | +83.43% | $128,555,561.14 |
| STG/USDT:USDT | +24.27% | $13,568,178.37 |
| UB/USDT:USDT | +19.95% | $1,773,728.74 |
| NAORIS/USDT:USDT | +15.64% | $1,567,623.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.70% | +4.71% |
| UAI/USDT:USDT | below_1h_threshold | +2.86% | +2.88% |
| BILL/USDT:USDT | below_1h_threshold | +2.75% | +2.77% |
| STG/USDT:USDT | below_1h_threshold | +2.71% | +2.73% |
| SPX/USDT:USDT | below_1h_threshold | +2.69% | +2.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
