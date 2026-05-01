# Decision Report

- generated_at: 2026-05-01T12:16:47.965194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2793**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2793, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.22% | **+3.22%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.80% | **+2.28%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.91% | **+2.04%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.59% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T12:16:46.217862+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=77592.1
- Funnel: target 760 → liquid 197 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +64.19% | $13,081,843.06 |
| UB/USDT:USDT | +48.31% | $18,497,266.68 |
| BR/USDT:USDT | +40.70% | $25,192,668.19 |
| ORCA/USDT:USDT | +35.87% | $11,031,630.91 |
| NFP/USDT:USDT | +32.09% | $1,231,044.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +5.00% | +4.79% |
| ORCA/USDT:USDT | below_1h_threshold | +4.08% | +3.87% |
| NFP/USDT:USDT | below_1h_threshold | +2.93% | +2.72% |
| ST/USDT:USDT | below_1h_threshold | +2.78% | +2.57% |
| AIOT/USDT:USDT | below_1h_threshold | +2.67% | +2.46% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
