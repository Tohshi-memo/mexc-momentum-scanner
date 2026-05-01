# Decision Report

- generated_at: 2026-05-01T23:09:07.438481+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2841**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=2841, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.26% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.36% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.16% | **+0.86%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.32% | **+0.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T23:09:05.560603+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78120.1
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +49.74% | $11,694,466.78 |
| CHILLGUY/USDT:USDT | +14.16% | $1,049,269.09 |
| WOJAK/USDT:USDT | +13.82% | $1,052,935.53 |
| RLS/USDT:USDT | +9.44% | $2,541,534.81 |
| BLESS/USDT:USDT | +9.24% | $1,150,221.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WOJAK/USDT:USDT | below_1h_threshold | +2.64% | +2.63% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +1.25% | +1.24% |
| VELVET/USDT:USDT | below_1h_threshold | +1.00% | +0.98% |
| B/USDT:USDT | below_1h_threshold | +0.79% | +0.77% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.63% | +0.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
