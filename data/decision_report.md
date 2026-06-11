# Decision Report

- generated_at: 2026-06-11T17:29:33.853729+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6383**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6383, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.07% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.79% | **+0.35%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.36% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.52** / 初期 $100.00 (+51.52%)
- 確定: 1300件 (Win 334 / Loss 413 / Flat 553) / skip 1644件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $151.52

## 4. Latest Market Context

- 更新: 2026-06-11T17:29:27.693050+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=62645.3
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +21.93% | $9,640,013.26 |
| SKYAI/USDT:USDT | +11.73% | $10,473,836.76 |
| VELVET/USDT:USDT | +9.09% | $93,615,619.50 |
| MAGMA/USDT:USDT | +9.01% | $1,639,037.21 |
| ZBT/USDT:USDT | +5.58% | $1,134,632.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.68% | +4.52% |
| VELVET/USDT:USDT | below_1h_threshold | +4.21% | +4.05% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.20% | +4.04% |
| A/USDT:USDT | below_1h_threshold | +4.11% | +3.95% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
