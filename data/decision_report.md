# Decision Report

- generated_at: 2026-06-11T22:55:12.979570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6422**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=6422, expectancy=-0.06%
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
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.85% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.42% | **+0.30%** |
| ASK_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1656件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-11T22:55:06.579485+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63492.8
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1, 4h RSI 84.4 >= 65=1, 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +103.63% | $19,373,460.30 |
| VELVET/USDT:USDT | +83.61% | $129,722,065.51 |
| STG/USDT:USDT | +27.53% | $13,748,754.73 |
| UB/USDT:USDT | +21.44% | $1,785,365.36 |
| NAORIS/USDT:USDT | +16.46% | $1,575,082.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.25% | +3.23% |
| SPX/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| BEAT/USDT:USDT | below_1h_threshold | +2.82% | +2.80% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.70% | +2.68% |
| SOXL/USDT:USDT | below_1h_threshold | +2.62% | +2.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
