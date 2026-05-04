# Decision Report

- generated_at: 2026-05-04T06:12:12.308278+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3164**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3164, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.31% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_BB3S | 2/11 | 18.2% | +2.74% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +0.27% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T06:12:10.404221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79922.9
- Funnel: target 758 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.95% | $23,376,595.63 |
| TAG/USDT:USDT | +58.59% | $8,173,859.38 |
| SKYAI/USDT:USDT | +56.48% | $46,866,403.44 |
| LAB/USDT:USDT | +45.91% | $214,514,816.27 |
| TST/USDT:USDT | +37.28% | $6,558,751.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +3.51% | +3.58% |
| LAB/USDT:USDT | below_1h_threshold | +3.37% | +3.44% |
| XVG/USDT:USDT | below_1h_threshold | +1.82% | +1.90% |
| BSB/USDT:USDT | below_1h_threshold | +1.58% | +1.66% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.56% | +1.64% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
