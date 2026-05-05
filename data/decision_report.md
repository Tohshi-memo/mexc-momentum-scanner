# Decision Report

- generated_at: 2026-05-05T04:42:34.754414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3306**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=3306, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/11 | 36.4% | +2.00% | **+0.73%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.93% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.38% | **+0.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.04% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T04:42:29.747818+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80743.4
- Funnel: target 764 → liquid 204 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +74.69% | $6,693,401.47 |
| FHE/USDT:USDT | +29.36% | $3,453,636.18 |
| 4/USDT:USDT | +22.96% | $2,201,693.31 |
| TONCOIN/USDT:USDT | +18.10% | $64,230,037.28 |
| NOT/USDT:USDT | +18.00% | $2,294,811.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +2.76% | +2.88% |
| SPACE/USDT:USDT | below_1h_threshold | +2.62% | +2.74% |
| LUNC/USDT:USDT | below_1h_threshold | +2.59% | +2.70% |
| 4/USDT:USDT | below_1h_threshold | +1.66% | +1.78% |
| PLAY/USDT:USDT | below_1h_threshold | +1.50% | +1.61% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
