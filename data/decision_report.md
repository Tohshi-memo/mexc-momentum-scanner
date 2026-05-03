# Decision Report

- generated_at: 2026-05-03T18:22:05.774851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3097**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3097, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.78% | **+0.98%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_ATR | 5/20 | 25.0% | +2.28% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.70% | **+2.59%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.32% | **+1.85%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.09% | **+1.85%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.09% | **+1.39%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T18:22:03.967841+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78650.1
- Funnel: target 755 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +46.16% | $309,477,711.77 |
| SKYAI/USDT:USDT | +14.46% | $24,631,123.49 |
| TST/USDT:USDT | +10.08% | $5,387,268.34 |
| BB/USDT:USDT | +7.48% | $1,374,303.95 |
| ASTEROID/USDT:USDT | +6.41% | $2,049,633.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +3.05% | +3.10% |
| LAB/USDT:USDT | below_1h_threshold | +2.34% | +2.40% |
| H/USDT:USDT | below_1h_threshold | +2.12% | +2.18% |
| ZBT/USDT:USDT | below_1h_threshold | +1.90% | +1.96% |
| BR/USDT:USDT | below_1h_threshold | +1.37% | +1.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
