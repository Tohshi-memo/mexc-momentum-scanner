# Decision Report

- generated_at: 2026-05-05T04:57:24.221523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3308**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=3308, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.00% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.45% | **+0.43%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.20% | **+0.08%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.35% | **-0.35%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.55% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T04:57:19.755791+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80854.9
- Funnel: target 764 → liquid 205 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +77.60% | $6,932,246.81 |
| FHE/USDT:USDT | +26.25% | $3,567,453.07 |
| 4/USDT:USDT | +19.34% | $2,258,028.69 |
| TONCOIN/USDT:USDT | +17.10% | $64,580,362.98 |
| NOT/USDT:USDT | +15.63% | $2,373,941.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.66% | +4.64% |
| LUNC/USDT:USDT | below_1h_threshold | +3.77% | +3.74% |
| SPACE/USDT:USDT | below_1h_threshold | +2.21% | +2.19% |
| DOGS/USDT:USDT | below_1h_threshold | +1.53% | +1.51% |
| PLAY/USDT:USDT | below_1h_threshold | +1.49% | +1.47% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
