# Decision Report

- generated_at: 2026-05-01T14:42:08.883848+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2812**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2812, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.18% | **+0.15%** |
| LIMIT_BB3S | 2/17 | 11.8% | +1.04% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.37% | **+1.90%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.99% | **+1.79%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.88% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.98% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:42:02.547115+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.71% price=78131.2
- Funnel: target 760 → liquid 201 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1, 4h RSI 84.5 >= 65=1, 4h RSI 69.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +117.06% | $26,432,616.03 |
| UB/USDT:USDT | +86.92% | $21,989,588.93 |
| NFP/USDT:USDT | +57.36% | $1,950,168.70 |
| BR/USDT:USDT | +39.63% | $26,337,753.14 |
| ZEREBRO/USDT:USDT | +36.93% | $12,238,415.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +4.14% |
| ST/USDT:USDT | below_1h_threshold | +2.16% | +2.87% |
| NFP/USDT:USDT | below_1h_threshold | +1.77% | +2.48% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.61% | +2.33% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.61% | +2.32% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
