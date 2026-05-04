# Decision Report

- generated_at: 2026-05-04T13:42:14.230495+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3206**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3206, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.38% | **+0.41%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.84% | **+2.27%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.07% | **+1.65%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.99% | **+1.35%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.86% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T13:42:12.143741+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78885.8
- Funnel: target 761 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +115.19% | $13,499,024.55 |
| SKYAI/USDT:USDT | +89.71% | $74,452,331.10 |
| GIGA/USDT:USDT | +54.75% | $2,130,171.93 |
| 4/USDT:USDT | +38.57% | $1,730,803.13 |
| GIGGLE/USDT:USDT | +28.70% | $4,047,479.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +4.45% | +4.36% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +4.32% | +4.24% |
| SIREN/USDT:USDT | below_1h_threshold | +3.61% | +3.52% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.38% | +3.29% |
| 4/USDT:USDT | below_1h_threshold | +3.31% | +3.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
