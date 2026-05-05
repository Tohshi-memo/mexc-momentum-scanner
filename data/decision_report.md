# Decision Report

- generated_at: 2026-05-05T05:22:25.228759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3310**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=3310, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.14% | **+2.14%** |
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.24% | **+0.68%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.68% | **+0.67%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.00% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.85% | **+0.43%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.48% | **+0.30%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.19% | **+0.02%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.18% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T05:22:20.553287+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80892.2
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +69.09% | $7,461,493.13 |
| HIVE/USDT:USDT | +38.51% | $1,126,365.43 |
| FHE/USDT:USDT | +27.04% | $3,653,029.61 |
| TONCOIN/USDT:USDT | +18.34% | $65,173,655.82 |
| RAVE/USDT:USDT | +15.66% | $63,998,625.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.91% | +3.86% |
| PLAY/USDT:USDT | below_1h_threshold | +2.27% | +2.22% |
| ALGO/USDT:USDT | below_1h_threshold | +2.05% | +2.00% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.58% | +1.53% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.30% | +1.25% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
