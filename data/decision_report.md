# Decision Report

- generated_at: 2026-05-01T12:26:50.242359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2794**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2794, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.63% | **+2.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.21% | **+2.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.46% | **+1.84%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.94% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T12:26:48.377528+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=77718.7
- Funnel: target 760 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +65.48% | $13,450,272.87 |
| UB/USDT:USDT | +53.34% | $18,846,226.23 |
| BR/USDT:USDT | +39.40% | $25,320,811.49 |
| ORCA/USDT:USDT | +34.59% | $11,144,938.24 |
| NFP/USDT:USDT | +34.43% | $1,254,895.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_relative_strength | +5.28% | +4.91% |
| ST/USDT:USDT | below_1h_threshold | +4.36% | +3.99% |
| NFP/USDT:USDT | below_1h_threshold | +4.12% | +3.74% |
| ORCA/USDT:USDT | below_1h_threshold | +3.00% | +2.62% |
| SILVER/USDT:USDT | below_1h_threshold | +1.99% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
