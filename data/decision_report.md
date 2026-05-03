# Decision Report

- generated_at: 2026-05-03T00:47:08.660317+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=3003, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 7/19 | 36.8% | +1.21% | **+0.45%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.45% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:47:03.870978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78593.5
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1, 4h RSI 94.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +22.74% | $1,968,392.64 |
| LUNC/USDT:USDT | +17.58% | $32,623,777.92 |
| BABY/USDT:USDT | +17.47% | $1,485,367.40 |
| BIANRENSHENG/USDT:USDT | +15.23% | $1,798,940.31 |
| SPACE/USDT:USDT | +12.70% | $1,759,246.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +2.73% | +2.81% |
| SPACE/USDT:USDT | below_1h_threshold | +2.47% | +2.54% |
| EDGE/USDT:USDT | below_1h_threshold | +2.33% | +2.41% |
| ORCA/USDT:USDT | below_1h_threshold | +1.40% | +1.48% |
| TAC/USDT:USDT | below_1h_threshold | +1.28% | +1.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
