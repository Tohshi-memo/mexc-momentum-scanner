# Decision Report

- generated_at: 2026-05-06T02:17:27.317307+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3406**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3406, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/10 | 50.0% | +2.27% | **+1.14%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.77% | **+1.11%** |
| ASK | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.09% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.06% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:17:25.047484+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=81224.6
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +34.18% | $1,268,073.09 |
| MAVIA/USDT:USDT | +28.52% | $1,703,921.32 |
| ZEC/USDT:USDT | +23.07% | $599,433,748.56 |
| NOT/USDT:USDT | +21.77% | $5,556,694.49 |
| SMCISTOCK/USDT:USDT | +19.69% | $5,204,085.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +3.82% | +4.02% |
| ZEC/USDT:USDT | below_1h_threshold | +2.11% | +2.31% |
| AKT/USDT:USDT | below_1h_threshold | +1.85% | +2.06% |
| STRK/USDT:USDT | below_1h_threshold | +1.54% | +1.74% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.31% | +1.51% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
