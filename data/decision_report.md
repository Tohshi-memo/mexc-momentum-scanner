# Decision Report

- generated_at: 2026-05-01T22:56:58.916845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2839**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=2839, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.77% | **+1.77%** |
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.23% | **+1.05%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.02% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.68% | **+0.76%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T22:56:57.014039+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78113.0
- Funnel: target 755 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +40.51% | $10,507,599.01 |
| CHILLGUY/USDT:USDT | +12.59% | $1,109,792.64 |
| RLS/USDT:USDT | +11.98% | $2,576,606.47 |
| BLESS/USDT:USDT | +9.01% | $1,132,276.94 |
| WOJAK/USDT:USDT | +8.87% | $1,058,236.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +2.39% | +2.45% |
| B/USDT:USDT | below_1h_threshold | +2.01% | +2.08% |
| TRB/USDT:USDT | below_1h_threshold | +1.57% | +1.64% |
| UAI/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |
| RLS/USDT:USDT | below_1h_threshold | +1.26% | +1.32% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
