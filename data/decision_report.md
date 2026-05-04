# Decision Report

- generated_at: 2026-05-04T00:47:17.091110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3117**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3117, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.08% | **+0.02%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_2PCT | 18/20 | 90.0% | -0.02% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +5.16% | **+2.58%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.78% | **+1.42%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.42% | **+0.78%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.07% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T00:47:14.764393+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=78386.0
- Funnel: target 756 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1, 4h RSI 83.4 >= 65=1, 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +47.21% | $30,057,866.52 |
| LAB/USDT:USDT | +44.82% | $250,059,208.80 |
| GIGA/USDT:USDT | +22.98% | $1,076,768.68 |
| PARTI/USDT:USDT | +19.16% | $1,336,516.81 |
| BSB/USDT:USDT | +16.37% | $15,136,127.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.83% | +5.01% |
| B/USDT:USDT | below_1h_threshold | +3.33% | +3.51% |
| BR/USDT:USDT | below_1h_threshold | +2.92% | +3.11% |
| UB/USDT:USDT | below_1h_threshold | +2.74% | +2.93% |
| BSB/USDT:USDT | below_1h_threshold | +2.71% | +2.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
