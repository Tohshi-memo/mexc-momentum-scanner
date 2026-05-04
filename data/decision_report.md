# Decision Report

- generated_at: 2026-05-04T02:32:31.014350+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3128**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3128, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 5/20 | 25.0% | +1.13% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.47% | **+1.74%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T02:32:28.538390+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79745.1
- Funnel: target 757 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1, 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +56.97% | $239,681,588.30 |
| SKYAI/USDT:USDT | +53.31% | $35,223,968.71 |
| TAG/USDT:USDT | +34.53% | $4,237,863.76 |
| GIGA/USDT:USDT | +23.51% | $1,101,459.04 |
| BSB/USDT:USDT | +20.57% | $14,930,282.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.50% | +4.50% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.37% | +3.38% |
| MONAD/USDT:USDT | below_1h_threshold | +2.26% | +2.26% |
| IP/USDT:USDT | below_1h_threshold | +1.74% | +1.74% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.69% | +1.69% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
