# Decision Report

- generated_at: 2026-05-30T03:55:14.474761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5100**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5100, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.72% | **-1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +7.43% | **+2.23%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_BB3S | 3/17 | 17.6% | +0.12% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.56% | **+2.56%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.70% | **+1.89%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.41% | **+1.45%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.82% | **+1.27%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +4.73% | **+1.18%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.84** / 初期 $100.00 (+25.84%)
- 確定: 758件 (Win 176 / Loss 227 / Flat 355) / skip 903件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HBAR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.84

## 4. Latest Market Context

- 更新: 2026-05-30T03:55:12.129362+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=73515.0
- Funnel: target 773 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +56.62% | $11,677,799.55 |
| XLM/USDT:USDT | +37.34% | $468,670,682.37 |
| ID/USDT:USDT | +18.97% | $5,748,015.22 |
| OL/USDT:USDT | +18.20% | $1,546,792.21 |
| LAB/USDT:USDT | +18.01% | $139,800,568.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +4.02% | +4.34% |
| XLM/USDT:USDT | below_1h_threshold | +2.79% | +3.10% |
| HEI/USDT:USDT | below_1h_threshold | +1.67% | +1.99% |
| VET/USDT:USDT | below_1h_threshold | +1.10% | +1.41% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
