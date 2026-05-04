# Decision Report

- generated_at: 2026-05-04T23:47:25.361028+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3279**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=3279, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_BB3S | 3/10 | 30.0% | +2.22% | **+0.67%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.57% | **+0.43%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.44% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.34% | **+0.33%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T23:47:22.672176+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=79736.7
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1, 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +24.78% | $55,723,560.95 |
| NAORIS/USDT:USDT | +23.07% | $4,312,108.79 |
| B3/USDT:USDT | +17.64% | $1,110,409.31 |
| FHE/USDT:USDT | +15.28% | $2,605,548.88 |
| TONCOIN/USDT:USDT | +12.94% | $39,198,087.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +1.89% | +2.26% |
| 4/USDT:USDT | below_1h_threshold | +1.69% | +2.05% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.39% | +1.76% |
| CHIP/USDT:USDT | below_1h_threshold | +1.04% | +1.41% |
| IP/USDT:USDT | below_1h_threshold | +0.99% | +1.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
