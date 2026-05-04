# Decision Report

- generated_at: 2026-05-04T00:37:18.256260+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3116**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3116, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.54% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.29% | **+0.28%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.08% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +5.03% | **+2.26%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.19% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T00:37:15.653040+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78358.9
- Funnel: target 756 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.5 >= 65=1, 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +41.47% | $29,284,497.17 |
| LAB/USDT:USDT | +32.54% | $248,261,190.27 |
| GIGA/USDT:USDT | +25.71% | $1,072,604.18 |
| BSB/USDT:USDT | +16.75% | $15,111,733.82 |
| PARTI/USDT:USDT | +15.31% | $1,320,036.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.78% | +3.99% |
| BSB/USDT:USDT | below_1h_threshold | +3.05% | +3.26% |
| BR/USDT:USDT | below_1h_threshold | +2.74% | +2.95% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.40% | +2.61% |
| AIOT/USDT:USDT | below_1h_threshold | +2.23% | +2.44% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
