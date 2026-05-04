# Decision Report

- generated_at: 2026-05-04T01:27:41.025536+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3123**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3123, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.23% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.47% | **+1.74%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.72% | **+1.20%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.42% | **+1.00%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.16% | **+0.93%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T01:27:38.482945+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78455.7
- Funnel: target 756 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1, 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +65.48% | $244,986,026.89 |
| SKYAI/USDT:USDT | +56.45% | $32,586,922.57 |
| TAG/USDT:USDT | +26.89% | $3,856,192.14 |
| GIGA/USDT:USDT | +21.55% | $1,087,179.34 |
| TRADOOR/USDT:USDT | +19.08% | $3,467,171.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +3.46% | +3.53% |
| UB/USDT:USDT | below_1h_threshold | +2.62% | +2.68% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.60% | +2.67% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.77% | +1.83% |
| B/USDT:USDT | below_1h_threshold | +1.60% | +1.66% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
