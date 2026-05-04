# Decision Report

- generated_at: 2026-05-04T06:57:05.371090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3166**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=3166, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.41% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_BB3S | 2/10 | 20.0% | +2.74% | **+0.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.65% | **+0.82%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.92% | **+0.65%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T06:57:03.515884+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=79902.3
- Funnel: target 758 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +53.12% | $48,595,463.75 |
| TAG/USDT:USDT | +50.42% | $10,115,916.25 |
| BSB/USDT:USDT | +48.96% | $24,776,103.35 |
| LAB/USDT:USDT | +38.70% | $216,754,782.51 |
| TST/USDT:USDT | +36.22% | $6,688,998.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +4.42% | +4.52% |
| SQD/USDT:USDT | below_1h_threshold | +4.09% | +4.19% |
| ALLO/USDT:USDT | below_1h_threshold | +2.68% | +2.78% |
| USTC/USDT:USDT | below_1h_threshold | +2.43% | +2.53% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.35% | +2.45% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
