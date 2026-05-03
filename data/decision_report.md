# Decision Report

- generated_at: 2026-05-03T17:02:10.927415+00:00
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

- 更新: 2026-05-03T17:02:09.147410+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78557.2
- Funnel: target 755 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +17.71% | $307,783,165.06 |
| SKYAI/USDT:USDT | +12.25% | $22,669,543.40 |
| AIOT/USDT:USDT | +6.04% | $2,159,030.40 |
| TST/USDT:USDT | +5.68% | $5,112,249.41 |
| BB/USDT:USDT | +4.21% | $1,242,074.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +1.37% | +1.45% |
| BB/USDT:USDT | below_1h_threshold | +1.10% | +1.18% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.54% | +0.62% |
| ORCA/USDT:USDT | below_1h_threshold | +0.53% | +0.61% |
| AKT/USDT:USDT | below_1h_threshold | +0.37% | +0.45% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
