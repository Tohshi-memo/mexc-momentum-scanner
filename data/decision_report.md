# Decision Report

- generated_at: 2026-05-04T18:07:25.357939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3246**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3246, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.22% | **+1.15%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.54% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T18:07:23.529859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80347.4
- Funnel: target 761 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +27.29% | $39,750,989.55 |
| TST/USDT:USDT | +11.92% | $21,570,250.34 |
| FHE/USDT:USDT | +9.71% | $2,783,920.08 |
| RAVE/USDT:USDT | +6.07% | $12,805,714.34 |
| SQD/USDT:USDT | +5.63% | $1,547,821.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +3.45% | +3.44% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.21% | +1.20% |
| LUNC/USDT:USDT | below_1h_threshold | +1.10% | +1.09% |
| FHE/USDT:USDT | below_1h_threshold | +1.07% | +1.06% |
| B3/USDT:USDT | below_1h_threshold | +0.86% | +0.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
