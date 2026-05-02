# Decision Report

- generated_at: 2026-05-02T17:02:12.985035+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2960**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2960, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.62% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.47% | **+0.35%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.67% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T17:02:11.223019+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78407.5
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +29.01% | $13,333,441.77 |
| LAB/USDT:USDT | +14.53% | $199,245,812.28 |
| TAC/USDT:USDT | +12.87% | $2,489,465.55 |
| XNY/USDT:USDT | +8.06% | $1,222,097.67 |
| ORDI/USDT:USDT | +7.42% | $25,941,140.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.35% | +1.36% |
| PNUT/USDT:USDT | below_1h_threshold | +1.09% | +1.10% |
| TAC/USDT:USDT | below_1h_threshold | +1.04% | +1.06% |
| BIO/USDT:USDT | below_1h_threshold | +1.02% | +1.03% |
| ORDI/USDT:USDT | below_1h_threshold | +1.01% | +1.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
