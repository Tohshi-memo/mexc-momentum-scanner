# Decision Report

- generated_at: 2026-05-04T00:27:20.494249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3114**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3114, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.78% | **+0.70%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.08% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +6.16% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.56% | **+1.79%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.55% | **+1.32%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T00:27:17.817567+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=78274.2
- Funnel: target 756 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1, 4h RSI 84.3 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +37.10% | $27,903,836.62 |
| LAB/USDT:USDT | +33.44% | $246,523,743.09 |
| GIGA/USDT:USDT | +27.19% | $1,059,403.41 |
| PARTI/USDT:USDT | +20.99% | $1,254,779.23 |
| BSB/USDT:USDT | +16.63% | $15,082,786.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +4.22% | +4.55% |
| BR/USDT:USDT | below_1h_threshold | +3.08% | +3.40% |
| BSB/USDT:USDT | below_1h_threshold | +2.94% | +3.27% |
| UB/USDT:USDT | below_1h_threshold | +2.58% | +2.91% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.96% | +2.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
