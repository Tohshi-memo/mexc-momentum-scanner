# Decision Report

- generated_at: 2026-05-05T23:22:44.517554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3400**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3400, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +2.11% | **+1.90%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.58% | **+0.36%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.75% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T23:22:42.548404+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81048.0
- Funnel: target 760 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAVIA/USDT:USDT | +23.55% | $1,506,515.70 |
| FHE/USDT:USDT | +23.49% | $25,740,536.73 |
| ZEC/USDT:USDT | +20.02% | $583,807,006.41 |
| SWARMS/USDT:USDT | +19.97% | $2,358,445.42 |
| SMCISTOCK/USDT:USDT | +17.67% | $5,041,037.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +1.69% | +1.72% |
| ZEC/USDT:USDT | below_1h_threshold | +1.53% | +1.56% |
| NOT/USDT:USDT | below_1h_threshold | +1.44% | +1.47% |
| AKT/USDT:USDT | below_1h_threshold | +1.35% | +1.37% |
| DOGS/USDT:USDT | below_1h_threshold | +1.20% | +1.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
