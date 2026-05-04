# Decision Report

- generated_at: 2026-05-04T18:02:34.335255+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3245, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.58% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.54% | **+0.54%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T18:02:32.323651+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80291.5
- Funnel: target 761 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +27.63% | $39,010,979.85 |
| TST/USDT:USDT | +18.79% | $21,346,238.74 |
| FHE/USDT:USDT | +9.15% | $2,766,902.59 |
| RAVE/USDT:USDT | +8.24% | $12,637,854.57 |
| SQD/USDT:USDT | +5.31% | $1,547,223.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +1.98% | +2.04% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.58% | +0.64% |
| FHE/USDT:USDT | below_1h_threshold | +0.56% | +0.62% |
| ON/USDT:USDT | below_1h_threshold | +0.48% | +0.54% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.39% | +0.46% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
