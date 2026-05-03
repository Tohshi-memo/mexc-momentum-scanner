# Decision Report

- generated_at: 2026-05-03T12:22:14.534792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3064**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3064, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.21% | **+0.17%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -0.30% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.02% | **+2.26%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.97% | **+1.63%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T12:22:12.730562+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=78747.2
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +42.47% | $2,859,579.25 |
| BABY/USDT:USDT | +35.01% | $19,328,930.20 |
| TAC/USDT:USDT | +29.51% | $2,052,703.62 |
| FHE/USDT:USDT | +26.50% | $3,754,660.60 |
| AIGENSYN/USDT:USDT | +24.97% | $4,443,813.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.83% | +3.67% |
| TAC/USDT:USDT | below_1h_threshold | +2.77% | +2.61% |
| BABY/USDT:USDT | below_1h_threshold | +2.45% | +2.29% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.33% | +2.17% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.27% | +1.11% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
