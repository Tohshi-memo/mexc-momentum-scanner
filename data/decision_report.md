# Decision Report

- generated_at: 2026-05-04T23:42:21.123037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3278**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3278, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.03% | **+0.83%** |
| LIMIT_BB3S | 3/10 | 30.0% | +2.22% | **+0.67%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.44% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.49% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.34% | **+0.33%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.36% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T23:42:18.754403+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=79773.8
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +25.67% | $55,419,634.59 |
| NAORIS/USDT:USDT | +21.96% | $4,138,102.54 |
| B3/USDT:USDT | +21.48% | $1,104,147.72 |
| FHE/USDT:USDT | +15.33% | $2,604,189.18 |
| TONCOIN/USDT:USDT | +13.04% | $38,764,271.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.23% | +2.55% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.02% | +2.34% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.57% | +1.89% |
| WLFI/USDT:USDT | below_1h_threshold | +0.94% | +1.27% |
| CHIP/USDT:USDT | below_1h_threshold | +0.89% | +1.21% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
