# Decision Report

- generated_at: 2026-05-01T18:37:04.026871+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2822**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=2822, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.54% | **+0.49%** |
| LIMIT_BB3S | 2/16 | 12.5% | +3.33% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +0.44% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T18:37:02.348714+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78485.2
- Funnel: target 756 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +14.83% | $1,793,950.09 |
| ZEC/USDT:USDT | +8.12% | $326,198,145.31 |
| MAGMA/USDT:USDT | +8.04% | $1,052,338.08 |
| ZEN/USDT:USDT | +6.84% | $4,416,475.41 |
| MEGA/USDT:USDT | +5.90% | $5,266,251.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +4.15% | +4.18% |
| TAG/USDT:USDT | below_1h_threshold | +2.91% | +2.94% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.84% | +2.87% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.28% | +2.31% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.01% | +2.04% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
