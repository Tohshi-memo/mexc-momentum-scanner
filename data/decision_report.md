# Decision Report

- generated_at: 2026-05-03T01:12:01.379918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3006**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=3006, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.00% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.21% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.41% | **+6.41%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.68% | **+0.84%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T01:11:59.530177+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=78303.5
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +19.54% | $33,317,034.14 |
| BABY/USDT:USDT | +16.60% | $1,686,650.60 |
| BIANRENSHENG/USDT:USDT | +16.18% | $1,833,833.28 |
| TRADOOR/USDT:USDT | +13.83% | $1,298,915.86 |
| SPACE/USDT:USDT | +11.84% | $1,775,898.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.99% | +2.24% |
| SIREN/USDT:USDT | below_1h_threshold | +1.24% | +1.49% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.02% | +1.27% |
| USTC/USDT:USDT | below_1h_threshold | +0.89% | +1.14% |
| LYN/USDT:USDT | below_1h_threshold | +0.76% | +1.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
