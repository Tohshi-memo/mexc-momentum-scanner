# Decision Report

- generated_at: 2026-05-03T17:04:48.799921+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3090**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3090, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_BB3S | 6/16 | 37.5% | +1.48% | **+0.55%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.98% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.92% | **+1.15%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.11% | **+1.05%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T17:04:46.948369+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=78550.0
- Funnel: target 755 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +17.06% | $308,009,657.75 |
| SKYAI/USDT:USDT | +12.51% | $22,733,248.12 |
| AIOT/USDT:USDT | +6.38% | $2,167,722.05 |
| TST/USDT:USDT | +5.46% | $5,120,488.30 |
| BR/USDT:USDT | +3.98% | $4,141,067.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +1.66% | +1.74% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.84% | +0.92% |
| BR/USDT:USDT | below_1h_threshold | +0.69% | +0.78% |
| WLFI/USDT:USDT | below_1h_threshold | +0.50% | +0.59% |
| MOVR/USDT:USDT | below_1h_threshold | +0.42% | +0.51% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
