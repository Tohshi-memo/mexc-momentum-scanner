# Decision Report

- generated_at: 2026-05-01T07:51:01.656198+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2763**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=2763, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.08% | **+0.70%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.33% | **+0.25%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.40% | **+0.23%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.07% | **+0.06%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:50:56.937526+00:00 / 保存件数 234/288
- BTC: STAGNANT 1h +0.15% price=77070.2
- Funnel: target 760 → liquid 206 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +57.70% | $2,205,471.34 |
| ZEREBRO/USDT:USDT | +47.10% | $4,561,229.86 |
| ORCA/USDT:USDT | +29.06% | $10,168,414.08 |
| BR/USDT:USDT | +20.11% | $20,199,002.61 |
| GENIUS/USDT:USDT | +17.59% | $1,589,726.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.82% | +2.67% |
| MYX/USDT:USDT | below_1h_threshold | +2.54% | +2.39% |
| DRIFT/USDT:USDT | below_1h_threshold | +1.90% | +1.75% |
| COAI/USDT:USDT | below_1h_threshold | +1.59% | +1.44% |
| DASH/USDT:USDT | below_1h_threshold | +1.24% | +1.09% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
