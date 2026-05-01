# Decision Report

- generated_at: 2026-05-01T10:42:03.200161+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2785**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2785, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.93% | **+3.70%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.45% | **+2.07%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T10:41:58.823854+00:00 / 保存件数 269/288
- BTC: STAGNANT 1h -0.01% price=77229.0
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +64.42% | $10,033,281.96 |
| UB/USDT:USDT | +56.61% | $13,538,121.60 |
| ZEREBRO/USDT:USDT | +46.16% | $8,405,671.00 |
| BR/USDT:USDT | +37.20% | $23,795,010.58 |
| ORCA/USDT:USDT | +29.87% | $10,648,012.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.16% | +3.18% |
| SIREN/USDT:USDT | below_1h_threshold | +2.65% | +2.66% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.28% | +2.30% |
| ZBT/USDT:USDT | below_1h_threshold | +1.72% | +1.73% |
| BRETT/USDT:USDT | below_1h_threshold | +1.37% | +1.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
