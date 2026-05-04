# Decision Report

- generated_at: 2026-05-04T14:27:12.850381+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3215**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3215, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.34% | **+3.34%** |
| ASK_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.70% | **+1.10%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T14:27:10.733009+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.71% price=79305.5
- Funnel: target 761 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +116.47% | $16,045,973.25 |
| SKYAI/USDT:USDT | +97.23% | $81,061,931.49 |
| GIGA/USDT:USDT | +44.12% | $2,220,400.79 |
| 4/USDT:USDT | +41.86% | $1,823,944.39 |
| ASTEROID/USDT:USDT | +29.35% | $4,311,202.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.09% | +3.38% |
| ZBT/USDT:USDT | below_1h_threshold | +2.73% | +2.02% |
| PARTI/USDT:USDT | below_1h_threshold | +2.39% | +1.68% |
| ORDI/USDT:USDT | below_1h_threshold | +2.38% | +1.67% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.89% | +1.18% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
