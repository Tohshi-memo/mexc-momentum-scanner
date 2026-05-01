# Decision Report

- generated_at: 2026-05-01T13:36:58.709793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2802**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2802, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.75% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.61% | **+2.48%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.37% | **+1.90%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T13:36:56.657720+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.71% price=78400.0
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +84.06% | $16,951,556.82 |
| UB/USDT:USDT | +64.07% | $20,662,719.80 |
| BR/USDT:USDT | +43.41% | $25,769,753.49 |
| NFP/USDT:USDT | +41.75% | $1,557,825.30 |
| ORCA/USDT:USDT | +36.14% | $11,633,491.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_relative_strength | +5.21% | +4.50% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.81% | +4.10% |
| BR/USDT:USDT | below_1h_threshold | +3.62% | +2.91% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +3.00% | +2.29% |
| INTUSTOCK/USDT:USDT | below_1h_threshold | +2.33% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
