# Decision Report

- generated_at: 2026-04-30T18:01:13.895954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2726**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2726, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.47% | **+2.47%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +6.55% | **+2.29%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| ASK_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T18:01:12.127815+00:00 / 保存件数 63/288
- BTC: STAGNANT 1h +0.14% price=76313.7
- Funnel: target 757 → liquid 229 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +24.97% | $12,986,822.36 |
| BR/USDT:USDT | +20.73% | $5,565,308.81 |
| ASTEROID/USDT:USDT | +7.20% | $3,780,144.89 |
| BIO/USDT:USDT | +6.80% | $3,707,558.83 |
| RIVER/USDT:USDT | +4.53% | $24,984,041.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.63% | +1.49% |
| ZEC/USDT:USDT | below_1h_threshold | +0.66% | +0.52% |
| PENGU/USDT:USDT | below_1h_threshold | +0.46% | +0.32% |
| ORDI/USDT:USDT | below_1h_threshold | +0.46% | +0.32% |
| DASH/USDT:USDT | below_1h_threshold | +0.34% | +0.20% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
