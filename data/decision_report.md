# Decision Report

- generated_at: 2026-05-01T14:57:01.706088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2816**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2816, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.72% | **+0.18%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.15% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.31% | **+1.18%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.31% | **+0.98%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:56:56.728381+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=78338.6
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1, 4h RSI 84.4 >= 65=1, 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +119.10% | $28,347,635.88 |
| UB/USDT:USDT | +86.24% | $22,469,855.22 |
| NFP/USDT:USDT | +52.45% | $2,069,642.55 |
| BR/USDT:USDT | +38.33% | $26,420,268.82 |
| ZEREBRO/USDT:USDT | +32.63% | $12,468,304.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +4.37% | +4.82% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +4.12% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.25% | +2.70% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.74% | +2.19% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.69% | +2.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
