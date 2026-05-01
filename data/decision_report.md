# Decision Report

- generated_at: 2026-05-01T07:16:02.618888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2760**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=2760, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.91% | **+0.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.74% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.15% | **+0.72%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.46% | **+0.35%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.18% | **+0.13%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:16:00.790813+00:00 / 保存件数 227/288
- BTC: STAGNANT 1h +0.05% price=76988.6
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +51.51% | $1,058,166.63 |
| ZEREBRO/USDT:USDT | +47.05% | $3,596,594.32 |
| ORCA/USDT:USDT | +29.13% | $10,056,814.98 |
| BR/USDT:USDT | +27.89% | $19,052,138.12 |
| GENIUS/USDT:USDT | +21.68% | $1,543,676.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.99% | +2.94% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.95% | +1.91% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.68% | +1.63% |
| VINE/USDT:USDT | below_1h_threshold | +1.48% | +1.43% |
| EDU/USDT:USDT | below_1h_threshold | +1.31% | +1.26% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
