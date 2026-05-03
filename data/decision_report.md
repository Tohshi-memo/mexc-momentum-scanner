# Decision Report

- generated_at: 2026-05-03T00:52:12.202505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3004**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=3004, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.21% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.50% | **+0.45%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.41% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.41% | **+6.41%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.88% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:52:09.660418+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=78469.5
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1, 4h RSI 69.4 >= 65=1, 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +24.29% | $1,989,656.20 |
| LUNC/USDT:USDT | +17.88% | $32,687,021.95 |
| BABY/USDT:USDT | +15.50% | $1,529,536.04 |
| BIANRENSHENG/USDT:USDT | +15.40% | $1,816,327.30 |
| TRADOOR/USDT:USDT | +15.05% | $1,163,881.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.03% | +4.27% |
| SPACE/USDT:USDT | below_1h_threshold | +2.61% | +2.84% |
| EDGE/USDT:USDT | below_1h_threshold | +2.50% | +2.73% |
| LUNC/USDT:USDT | below_1h_threshold | +1.18% | +1.41% |
| ORCA/USDT:USDT | below_1h_threshold | +1.06% | +1.29% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
