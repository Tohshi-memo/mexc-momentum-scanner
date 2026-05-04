# Decision Report

- generated_at: 2026-05-04T14:32:29.377704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3217**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3217, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.07% | **+2.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| ASK_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.46% | **+1.09%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T14:32:27.146974+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=79272.4
- Funnel: target 761 → liquid 195 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +121.23% | $16,240,880.62 |
| SKYAI/USDT:USDT | +91.37% | $82,117,813.62 |
| GIGA/USDT:USDT | +44.35% | $2,229,344.45 |
| 4/USDT:USDT | +38.66% | $1,831,294.26 |
| ASTEROID/USDT:USDT | +30.06% | $4,326,435.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.14% | +3.48% |
| TST/USDT:USDT | below_1h_threshold | +3.45% | +2.79% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.39% | +2.73% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.69% | +2.02% |
| ORDI/USDT:USDT | below_1h_threshold | +2.65% | +1.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
