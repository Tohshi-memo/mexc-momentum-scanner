# Decision Report

- generated_at: 2026-06-12T00:55:48.059995+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6434**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6434, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.79% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.30% | **+0.11%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.31% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.67% | **+1.17%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.95%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.86% | **+0.84%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.31% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1668件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T00:55:42.052389+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63676.7
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1, 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +94.57% | $130,173,438.31 |
| ESPORTS/USDT:USDT | +73.43% | $25,684,761.88 |
| H/USDT:USDT | +27.89% | $35,613,635.72 |
| XPL/USDT:USDT | +18.80% | $3,002,864.08 |
| UB/USDT:USDT | +17.20% | $1,872,090.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.26% | +4.13% |
| BSB/USDT:USDT | below_1h_threshold | +2.61% | +2.48% |
| BILL/USDT:USDT | below_1h_threshold | +2.39% | +2.26% |
| ALLO/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
