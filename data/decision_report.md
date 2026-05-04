# Decision Report

- generated_at: 2026-05-04T20:07:16.894057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3255**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3255, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.83% | **+0.57%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.54% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.91% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.14% | **+2.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.24% | **+1.34%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.93% | **+0.68%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.59% | **+0.63%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.66% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T20:07:14.769255+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79989.9
- Funnel: target 760 → liquid 198 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +45.15% | $25,604,013.83 |
| SKYAI/USDT:USDT | +13.75% | $97,506,246.51 |
| TST/USDT:USDT | +12.89% | $22,384,079.81 |
| LUNC/USDT:USDT | +7.85% | $69,913,188.17 |
| GIGGLE/USDT:USDT | +7.68% | $5,424,670.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.50% | +4.54% |
| TST/USDT:USDT | below_1h_threshold | +2.40% | +2.44% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.50% | +1.54% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.86% | +0.90% |
| AIOZ/USDT:USDT | below_1h_threshold | +0.75% | +0.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
