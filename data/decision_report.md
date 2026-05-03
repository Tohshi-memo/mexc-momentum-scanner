# Decision Report

- generated_at: 2026-05-03T06:37:01.957395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3042**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3042, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/12 | 66.7% | +1.80% | **+1.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.81% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.18% | **+1.31%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.65% | **+0.83%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.96% | **+0.38%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.28% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T06:36:59.935860+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78121.0
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +47.39% | $4,684,797.55 |
| BR/USDT:USDT | +27.96% | $2,655,139.16 |
| BSB/USDT:USDT | +14.11% | $14,798,152.33 |
| AIGENSYN/USDT:USDT | +13.57% | $2,329,020.04 |
| AKT/USDT:USDT | +12.87% | $1,341,838.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.91% | +5.02% |
| TAC/USDT:USDT | below_1h_threshold | +2.87% | +2.98% |
| ORBS/USDT:USDT | below_1h_threshold | +2.18% | +2.30% |
| BSB/USDT:USDT | below_1h_threshold | +2.06% | +2.17% |
| XNY/USDT:USDT | below_1h_threshold | +1.37% | +1.48% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
