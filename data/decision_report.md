# Decision Report

- generated_at: 2026-04-30T17:16:01.441297+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2721**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2721, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.11% | **+0.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +5.66% | **+2.55%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +4.77% | **+2.39%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.27% | **+1.47%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.91% | **+1.24%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T17:15:59.930020+00:00 / 保存件数 54/288
- BTC: STAGNANT 1h -0.08% price=76156.1
- Funnel: target 761 → liquid 228 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +9.33% | $6,110,321.87 |
| BR/USDT:USDT | +8.48% | $4,473,887.27 |
| ASTEROID/USDT:USDT | +6.49% | $3,682,876.05 |
| AIOT/USDT:USDT | +6.42% | $11,803,716.29 |
| BIO/USDT:USDT | +5.07% | $3,636,402.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.09% | +3.17% |
| BLEND/USDT:USDT | below_1h_threshold | +2.20% | +2.28% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.12% | +2.20% |
| CHIP/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |
| RIVER/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
