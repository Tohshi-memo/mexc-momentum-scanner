# Decision Report

- generated_at: 2026-06-12T01:20:54.202884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6438, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.98% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.04% | **+0.21%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.48% | **+0.11%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.85% | **+1.30%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.31% | **+1.15%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.60% | **+1.04%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +3.22% | **+0.97%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.94% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1672件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T01:20:48.901150+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=63377.2
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +92.56% | $128,616,446.37 |
| ESPORTS/USDT:USDT | +66.88% | $26,096,714.20 |
| H/USDT:USDT | +25.24% | $36,401,659.37 |
| UB/USDT:USDT | +18.31% | $1,811,874.58 |
| SKYAI/USDT:USDT | +18.19% | $13,326,092.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.35% | +3.72% |
| BILL/USDT:USDT | below_1h_threshold | +1.13% | +1.50% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.95% | +1.32% |
| XMR/USDT:USDT | below_1h_threshold | +0.93% | +1.30% |
| UB/USDT:USDT | below_1h_threshold | +0.73% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
