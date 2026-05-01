# Decision Report

- generated_at: 2026-05-01T17:06:56.229757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2821**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2821, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 2/16 | 12.5% | +3.33% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T17:06:54.509374+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78128.9
- Funnel: target 760 → liquid 195 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEC/USDT:USDT | +5.10% | $287,943,545.98 |
| B/USDT:USDT | +4.43% | $41,774,064.76 |
| DASH/USDT:USDT | +3.99% | $8,197,120.49 |
| BAS/USDT:USDT | +3.85% | $1,006,609.25 |
| MAGMA/USDT:USDT | +3.48% | $1,056,142.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +0.86% | +0.92% |
| MEGA/USDT:USDT | below_1h_threshold | +0.85% | +0.91% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.63% | +0.69% |
| CYS/USDT:USDT | below_1h_threshold | +0.60% | +0.66% |
| B/USDT:USDT | below_1h_threshold | +0.55% | +0.61% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
