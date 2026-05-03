# Decision Report

- generated_at: 2026-05-03T00:27:07.671222+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3001**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3001, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.23% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.51% | **+0.90%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.99% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:27:05.873352+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78593.1
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +24.69% | $1,624,675.16 |
| LUNC/USDT:USDT | +15.60% | $30,066,523.40 |
| XNY/USDT:USDT | +15.38% | $2,289,030.64 |
| BIANRENSHENG/USDT:USDT | +15.13% | $1,738,896.26 |
| NAORIS/USDT:USDT | +12.59% | $4,569,566.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.77% | +4.84% |
| FHE/USDT:USDT | below_1h_threshold | +4.20% | +4.28% |
| BABY/USDT:USDT | below_1h_threshold | +3.23% | +3.31% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.95% | +3.02% |
| BIO/USDT:USDT | below_1h_threshold | +1.81% | +1.89% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
