# Decision Report

- generated_at: 2026-05-01T11:26:56.344259+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2791**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2791, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.22% | **+3.22%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.81% | **+1.82%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.13% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T11:26:54.676779+00:00 / 保存件数 279/288
- BTC: STAGNANT 1h +0.10% price=77345.0
- Funnel: target 760 → liquid 197 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +61.93% | $10,977,890.30 |
| ZEREBRO/USDT:USDT | +51.58% | $9,002,845.34 |
| BR/USDT:USDT | +41.76% | $24,675,122.88 |
| UB/USDT:USDT | +35.76% | $17,247,056.68 |
| ORCA/USDT:USDT | +28.18% | $10,766,799.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ST/USDT:USDT | below_1h_threshold | +4.67% | +4.57% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.44% | +3.35% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.77% | +2.68% |
| NOM/USDT:USDT | below_1h_threshold | +2.24% | +2.14% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.70% | +1.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
