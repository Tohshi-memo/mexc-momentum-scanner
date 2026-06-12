# Decision Report

- generated_at: 2026-06-12T00:49:42.183583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6433**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6433, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.79% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.30% | **+0.11%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_BB3S | 3/18 | 16.7% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.02% | **+1.21%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.88% | **+1.01%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.94% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1667件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T00:49:36.318298+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63654.2
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +89.34% | $129,409,827.37 |
| ESPORTS/USDT:USDT | +74.15% | $25,542,360.01 |
| H/USDT:USDT | +26.35% | $35,414,122.75 |
| UB/USDT:USDT | +18.57% | $1,868,532.61 |
| XPL/USDT:USDT | +18.41% | $2,985,726.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.44% | +4.34% |
| BSB/USDT:USDT | below_1h_threshold | +2.75% | +2.66% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.64% | +2.54% |
| ALLO/USDT:USDT | below_1h_threshold | +2.33% | +2.24% |
| BILL/USDT:USDT | below_1h_threshold | +2.10% | +2.01% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
