# Decision Report

- generated_at: 2026-05-04T09:27:14.836696+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3175**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=3175, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.30% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.05% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:27:12.662418+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79776.5
- Funnel: target 761 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +64.98% | $7,788,436.51 |
| SKYAI/USDT:USDT | +57.63% | $49,482,859.22 |
| TAG/USDT:USDT | +48.55% | $13,484,496.44 |
| GIGA/USDT:USDT | +37.70% | $1,258,310.16 |
| 4/USDT:USDT | +32.35% | $1,235,829.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.72% | +3.59% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.58% | +3.44% |
| RSR/USDT:USDT | below_1h_threshold | +3.33% | +3.19% |
| GIGA/USDT:USDT | below_1h_threshold | +3.16% | +3.02% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.74% | +2.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
