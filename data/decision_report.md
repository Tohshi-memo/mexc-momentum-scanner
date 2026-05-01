# Decision Report

- generated_at: 2026-05-01T13:42:06.207724+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2803**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2803, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.75% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.98% | **+1.88%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.00% | **+1.70%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.69% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T13:42:03.795149+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=78127.9
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +82.85% | $17,480,072.78 |
| UB/USDT:USDT | +60.99% | $20,896,910.39 |
| BR/USDT:USDT | +45.38% | $25,913,963.91 |
| NFP/USDT:USDT | +41.91% | $1,569,641.13 |
| ORCA/USDT:USDT | +34.52% | $11,658,826.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_relative_strength | +5.16% | +4.80% |
| STXSTOCK/USDT:USDT | below_relative_strength | +5.10% | +4.74% |
| BR/USDT:USDT | below_1h_threshold | +4.90% | +4.54% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.32% | +3.96% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.00% | +3.64% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
