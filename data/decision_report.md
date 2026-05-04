# Decision Report

- generated_at: 2026-05-04T15:57:27.603503+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3229**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3229, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.05% | **+2.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T15:57:22.760336+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=79923.9
- Funnel: target 761 → liquid 203 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1, 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +120.89% | $1,917,057.14 |
| SKYAI/USDT:USDT | +84.03% | $92,069,910.58 |
| TST/USDT:USDT | +69.38% | $19,271,778.55 |
| GIGA/USDT:USDT | +38.77% | $2,326,820.14 |
| ASTEROID/USDT:USDT | +38.70% | $4,952,472.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.18% | +4.49% |
| DASH/USDT:USDT | below_1h_threshold | +4.05% | +4.35% |
| BSB/USDT:USDT | below_1h_threshold | +3.29% | +3.60% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.74% | +3.05% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.32% | +2.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
