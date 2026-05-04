# Decision Report

- generated_at: 2026-05-04T14:47:21.644134+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3218**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3218, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.44% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.07% | **+2.07%** |
| MARKET_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| ASK_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.85% | **+1.29%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.82% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T14:47:17.399626+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.09% price=79603.0
- Funnel: target 761 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +131.84% | $1,064,843.84 |
| SKYAI/USDT:USDT | +91.44% | $85,034,598.26 |
| TST/USDT:USDT | +90.98% | $17,300,049.55 |
| GIGA/USDT:USDT | +49.94% | $2,250,446.42 |
| 4/USDT:USDT | +31.46% | $1,862,937.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +5.00% | +3.91% |
| BANANAS31/USDT:USDT | below_1h_threshold | +4.72% | +3.64% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.42% | +2.34% |
| ZBT/USDT:USDT | below_1h_threshold | +3.39% | +2.31% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.31% | +2.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
