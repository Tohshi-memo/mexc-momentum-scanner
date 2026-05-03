# Decision Report

- generated_at: 2026-05-03T05:52:15.045186+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3039**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3039, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 7/11 | 63.6% | +0.92% | **+0.58%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.42% | **+1.57%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.92% | **+0.50%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:52:09.853123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78194.2
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 96.3 >= 65=1, 4h RSI 86.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +34.95% | $3,101,054.96 |
| BR/USDT:USDT | +21.82% | $2,425,378.45 |
| AKT/USDT:USDT | +18.25% | $1,282,554.47 |
| FIGHT/USDT:USDT | +12.92% | $1,023,402.58 |
| FHE/USDT:USDT | +10.84% | $2,557,573.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.17% | +4.09% |
| BB/USDT:USDT | below_1h_threshold | +4.17% | +4.09% |
| ALCH/USDT:USDT | below_1h_threshold | +3.06% | +2.98% |
| TRX/USDT:USDT | below_1h_threshold | +3.04% | +2.96% |
| BR/USDT:USDT | below_1h_threshold | +2.62% | +2.54% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
