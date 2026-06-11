# Decision Report

- generated_at: 2026-06-11T21:39:30.615543+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6413**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=6413, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.63% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.91% | **+0.32%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.32% | **+1.06%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | -0.04% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1647件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-11T21:39:27.332037+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63473.1
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 93.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +62.68% | $124,435,501.36 |
| ESPORTS/USDT:USDT | +55.27% | $15,454,085.40 |
| STG/USDT:USDT | +24.15% | $13,245,578.28 |
| NAORIS/USDT:USDT | +18.12% | $1,534,006.96 |
| XPL/USDT:USDT | +11.46% | $1,833,867.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.12% | +3.94% |
| UAI/USDT:USDT | below_1h_threshold | +2.83% | +2.65% |
| VVV/USDT:USDT | below_1h_threshold | +2.74% | +2.56% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.51% | +2.33% |
| NEAR/USDT:USDT | below_1h_threshold | +1.81% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
