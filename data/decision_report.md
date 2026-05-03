# Decision Report

- generated_at: 2026-05-03T05:47:24.524121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3037**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=3037, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| ASK | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 5/11 | 45.5% | +1.49% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.63% | **+0.41%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.39% | **+0.21%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:47:19.513926+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78178.1
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1, 4h RSI 95.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +30.30% | $2,982,633.89 |
| BR/USDT:USDT | +21.89% | $2,412,827.40 |
| AKT/USDT:USDT | +16.10% | $1,273,328.66 |
| FIGHT/USDT:USDT | +12.60% | $1,021,202.72 |
| FHE/USDT:USDT | +12.29% | $2,553,269.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +4.04% | +3.98% |
| AKT/USDT:USDT | below_1h_threshold | +3.99% | +3.93% |
| ALCH/USDT:USDT | below_1h_threshold | +3.51% | +3.45% |
| BSB/USDT:USDT | below_1h_threshold | +3.15% | +3.09% |
| TRX/USDT:USDT | below_1h_threshold | +2.95% | +2.89% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
