# Decision Report

- generated_at: 2026-05-03T00:32:34.672932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3001**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3001, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.23% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.51% | **+0.90%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.99% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:32:29.237983+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78601.3
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 93.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +28.51% | $1,693,269.82 |
| LUNC/USDT:USDT | +16.31% | $30,365,689.56 |
| BIANRENSHENG/USDT:USDT | +15.77% | $1,754,935.12 |
| SPACE/USDT:USDT | +15.20% | $1,720,340.84 |
| BABY/USDT:USDT | +14.35% | $1,446,687.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +4.74% | +4.81% |
| BIO/USDT:USDT | below_1h_threshold | +1.98% | +2.05% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |
| EDGE/USDT:USDT | below_1h_threshold | +1.25% | +1.32% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +0.79% | +0.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
