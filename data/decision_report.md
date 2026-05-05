# Decision Report

- generated_at: 2026-05-05T21:52:25.261867+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3393**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3393, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.39% | **+0.85%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.50% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.42% | **+1.94%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.23% | **+1.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.40% | **+1.08%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.94% | **+1.03%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.52% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:52:22.856938+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=81429.9
- Funnel: target 759 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1, 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAVIA/USDT:USDT | +29.84% | $1,299,365.26 |
| FHE/USDT:USDT | +28.33% | $21,346,850.69 |
| ZEC/USDT:USDT | +21.88% | $579,816,315.30 |
| SWARMS/USDT:USDT | +21.43% | $2,328,927.98 |
| SMCISTOCK/USDT:USDT | +18.82% | $4,857,982.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.93% | +5.15% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.98% | +4.20% |
| SWARMS/USDT:USDT | below_1h_threshold | +3.80% | +4.02% |
| DOGS/USDT:USDT | below_1h_threshold | +3.12% | +3.34% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.59% | +2.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
