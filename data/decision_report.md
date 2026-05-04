# Decision Report

- generated_at: 2026-05-04T16:42:26.548445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3236**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3236, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.50% | **-1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +4.94% | **+1.48%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.88% | **+1.13%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.87% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +6.04% | **+3.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T16:42:21.005613+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=80206.8
- Funnel: target 761 → liquid 203 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 66.9 >= 65=1, 4h RSI 82.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +15.69% | $34,802,763.50 |
| TST/USDT:USDT | +14.21% | $20,205,014.16 |
| TAG/USDT:USDT | +7.88% | $17,698,661.52 |
| AIOZ/USDT:USDT | +5.34% | $1,326,464.06 |
| B3/USDT:USDT | +4.71% | $1,013,817.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +4.89% | +4.61% |
| BABY/USDT:USDT | below_1h_threshold | +4.06% | +3.77% |
| UB/USDT:USDT | below_1h_threshold | +3.81% | +3.53% |
| FHE/USDT:USDT | below_1h_threshold | +3.53% | +3.24% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.43% | +3.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
