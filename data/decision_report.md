# Decision Report

- generated_at: 2026-05-01T11:46:37.761038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2792**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2792, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.22% | **+3.22%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.80% | **+2.28%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.13% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T11:46:36.251968+00:00 / 保存件数 283/288
- BTC: STAGNANT 1h +0.11% price=77356.8
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +67.82% | $11,830,007.08 |
| UB/USDT:USDT | +46.69% | $18,194,949.56 |
| NFP/USDT:USDT | +41.67% | $1,042,733.57 |
| BR/USDT:USDT | +38.65% | $24,896,545.54 |
| ZEREBRO/USDT:USDT | +31.16% | $9,807,577.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.45% | +3.33% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.24% | +3.13% |
| AIOT/USDT:USDT | below_1h_threshold | +3.21% | +3.09% |
| NOM/USDT:USDT | below_1h_threshold | +2.39% | +2.28% |
| ZBT/USDT:USDT | below_1h_threshold | +2.04% | +1.92% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
