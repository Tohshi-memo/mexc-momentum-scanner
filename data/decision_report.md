# Decision Report

- generated_at: 2026-04-30T23:01:13.517800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2741**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2741, expectancy=-0.11%
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
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.20% | **+2.88%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.11% | **+2.87%** |
| ASK_LONG | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.26% | **+2.13%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.02% | **+2.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T23:01:11.886999+00:00 / 保存件数 126/288
- BTC: STAGNANT 1h +0.02% price=76209.6
- Funnel: target 757 → liquid 212 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +22.19% | $14,265,148.93 |
| ORCA/USDT:USDT | +20.49% | $3,445,713.98 |
| DRIFT/USDT:USDT | +16.76% | $1,349,423.97 |
| AIOT/USDT:USDT | +16.56% | $17,970,645.53 |
| RDDTSTOCK/USDT:USDT | +14.09% | $3,923,186.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +0.71% | +0.70% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.71% | +0.69% |
| APE/USDT:USDT | below_1h_threshold | +0.44% | +0.43% |
| BR/USDT:USDT | below_1h_threshold | +0.40% | +0.39% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.34% | +0.32% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
