# Decision Report

- generated_at: 2026-05-01T17:02:12.981335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2820**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2820, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_BB3S | 2/16 | 12.5% | +3.33% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T17:02:11.244576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78242.5
- Funnel: target 760 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +5.27% | $41,597,328.42 |
| ZEC/USDT:USDT | +4.69% | $285,531,897.03 |
| BAS/USDT:USDT | +3.97% | $1,001,298.12 |
| DASH/USDT:USDT | +3.88% | $8,131,167.12 |
| ZEN/USDT:USDT | +3.57% | $2,504,859.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +1.42% | +1.34% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.14% | +1.06% |
| MEGA/USDT:USDT | below_1h_threshold | +1.04% | +0.96% |
| AR/USDT:USDT | below_1h_threshold | +0.62% | +0.53% |
| DASH/USDT:USDT | below_1h_threshold | +0.37% | +0.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
