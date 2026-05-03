# Decision Report

- generated_at: 2026-05-03T06:52:04.724080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3044**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3044, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/11 | 63.6% | +1.06% | **+0.67%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.68% | **+0.30%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.26% | **+0.23%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.76% | **+0.97%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T06:52:02.339106+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78180.0
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +42.68% | $5,025,865.31 |
| BR/USDT:USDT | +28.86% | $2,746,079.11 |
| AIGENSYN/USDT:USDT | +17.10% | $2,430,669.17 |
| BSB/USDT:USDT | +16.44% | $14,998,384.36 |
| FIGHT/USDT:USDT | +12.53% | $1,423,047.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.03% | +4.07% |
| TAC/USDT:USDT | below_1h_threshold | +3.61% | +3.65% |
| ORBS/USDT:USDT | below_1h_threshold | +1.86% | +1.90% |
| BR/USDT:USDT | below_1h_threshold | +1.80% | +1.84% |
| BABY/USDT:USDT | below_1h_threshold | +1.68% | +1.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
