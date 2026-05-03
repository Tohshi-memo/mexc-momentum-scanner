# Decision Report

- generated_at: 2026-05-03T03:32:13.037205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=3020, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| ASK | 20/20 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.84% | **+1.11%** |
| LIMIT_BB3S | 8/15 | 53.3% | +2.03% | **+1.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.82% | **+0.64%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.90% | **+0.27%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.77% | **+0.27%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.29% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T03:32:08.279202+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78108.2
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +17.02% | $1,435,077.58 |
| GENIUS/USDT:USDT | +16.12% | $1,007,588.53 |
| BIANRENSHENG/USDT:USDT | +13.33% | $2,175,742.85 |
| FHE/USDT:USDT | +12.95% | $2,424,875.24 |
| TAC/USDT:USDT | +10.87% | $2,699,410.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.23% | +3.26% |
| ALCH/USDT:USDT | below_1h_threshold | +2.83% | +2.86% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.18% | +2.21% |
| XNY/USDT:USDT | below_1h_threshold | +1.56% | +1.59% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.53% | +1.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
