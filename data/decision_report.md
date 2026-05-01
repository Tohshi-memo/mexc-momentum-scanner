# Decision Report

- generated_at: 2026-05-01T10:27:07.614052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2783**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2783, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.93% | **+3.70%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.45% | **+2.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.89%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T10:27:05.495010+00:00 / 保存件数 266/288
- BTC: STAGNANT 1h +0.13% price=77342.7
- Funnel: target 760 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1, 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +60.87% | $9,716,633.37 |
| UB/USDT:USDT | +46.81% | $12,798,412.22 |
| ZEREBRO/USDT:USDT | +46.25% | $8,093,010.46 |
| BR/USDT:USDT | +40.36% | $23,526,760.19 |
| ORCA/USDT:USDT | +31.22% | $10,575,002.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +2.95% | +2.81% |
| SIREN/USDT:USDT | below_1h_threshold | +2.43% | +2.29% |
| AIOT/USDT:USDT | below_1h_threshold | +2.32% | +2.18% |
| ORCA/USDT:USDT | below_1h_threshold | +1.78% | +1.64% |
| BRETT/USDT:USDT | below_1h_threshold | +1.56% | +1.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
