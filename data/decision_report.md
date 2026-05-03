# Decision Report

- generated_at: 2026-05-03T03:12:18.014937+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3019**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=3019, expectancy=-0.14%
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
| LIMIT_BB3S | 7/15 | 46.7% | +2.89% | **+1.35%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.09% | **+1.26%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.76% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.82% | **+0.64%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.90% | **+0.27%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.77% | **+0.27%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.35% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T03:12:16.229381+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78091.1
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIANRENSHENG/USDT:USDT | +15.59% | $2,145,532.81 |
| BABY/USDT:USDT | +12.32% | $1,874,414.98 |
| FHE/USDT:USDT | +12.09% | $2,401,304.77 |
| TRADOOR/USDT:USDT | +9.06% | $1,650,166.39 |
| TAC/USDT:USDT | +6.28% | $2,685,305.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +2.35% | +2.40% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |
| MOVR/USDT:USDT | below_1h_threshold | +1.45% | +1.50% |
| ORCA/USDT:USDT | below_1h_threshold | +1.10% | +1.15% |
| ALCH/USDT:USDT | below_1h_threshold | +1.05% | +1.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
