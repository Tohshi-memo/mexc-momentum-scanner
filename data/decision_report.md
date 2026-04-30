# Decision Report

- generated_at: 2026-04-30T23:26:01.005997+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2742**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2742, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.21% | **-2.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.97% | **+2.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.17% | **+2.29%** |
| ASK_LONG | 20/20 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.26% | **+2.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T23:25:59.236986+00:00 / 保存件数 131/288
- BTC: STAGNANT 1h +0.09% price=76263.2
- Funnel: target 757 → liquid 214 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +32.77% | $4,553,676.51 |
| BR/USDT:USDT | +23.39% | $14,606,046.27 |
| DRIFT/USDT:USDT | +18.73% | $1,408,357.88 |
| RDDTSTOCK/USDT:USDT | +13.58% | $4,026,273.25 |
| GENIUS/USDT:USDT | +13.30% | $1,141,719.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.19% | +2.11% |
| SIREN/USDT:USDT | below_1h_threshold | +2.02% | +1.94% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.49% | +1.41% |
| DRIFT/USDT:USDT | below_1h_threshold | +1.47% | +1.38% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.42% | +1.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
