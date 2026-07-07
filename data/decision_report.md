# Decision Report

- generated_at: 2026-07-07T15:56:16.394943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8443**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8443, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.32% | **+0.58%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.55% | **+1.09%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定トレード: 69件 (TP 23 / SL 45 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.55
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.09** / 初期 $100.00 (+222.09%)
- 確定: 2648件 (Win 845 / Loss 896 / Flat 907) / skip 2356件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANANA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $322.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1214件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0289 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T15:56:08.990570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.56% price=63889.7
- Funnel: target 847 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +106.08% | $18,761,943.48 |
| BLUR/USDT:USDT | +44.06% | $13,912,173.77 |
| EDGE/USDT:USDT | +29.50% | $7,323,073.79 |
| BANANA/USDT:USDT | +17.07% | $1,270,577.17 |
| M/USDT:USDT | +16.44% | $1,057,122.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.65% | +4.09% |
| CHIP/USDT:USDT | below_1h_threshold | +4.46% | +3.90% |
| DASH/USDT:USDT | below_1h_threshold | +2.75% | +2.20% |
| LDO/USDT:USDT | below_1h_threshold | +2.62% | +2.07% |
| UAI/USDT:USDT | below_1h_threshold | +2.32% | +1.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
