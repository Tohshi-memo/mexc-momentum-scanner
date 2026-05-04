# Decision Report

- generated_at: 2026-05-04T00:17:19.465197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3111**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3111, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.65% | **+0.50%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.08% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.72% | **+2.79%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +5.89% | **+2.06%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.97% | **+1.78%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.80% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T00:17:14.739175+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78436.0
- Funnel: target 756 → liquid 160 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1, 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +51.39% | $244,843,013.71 |
| SKYAI/USDT:USDT | +33.51% | $26,928,930.81 |
| GIGA/USDT:USDT | +31.05% | $1,047,843.63 |
| TAG/USDT:USDT | +14.38% | $3,700,572.37 |
| PARTI/USDT:USDT | +13.64% | $1,197,411.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.80% | +4.91% |
| AKT/USDT:USDT | below_1h_threshold | +4.30% | +4.42% |
| PARTI/USDT:USDT | below_1h_threshold | +3.84% | +3.96% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.98% | +2.10% |
| BR/USDT:USDT | below_1h_threshold | +1.96% | +2.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
