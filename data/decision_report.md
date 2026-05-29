# Decision Report

- generated_at: 2026-05-29T06:08:35.483668+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5017**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5017, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.32% | **+1.16%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.12% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.31** / 初期 $100.00 (+26.31%)
- 確定: 739件 (Win 175 / Loss 225 / Flat 339) / skip 839件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.31

## 4. Latest Market Context

- 更新: 2026-05-29T06:08:33.742669+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=73602.5
- Funnel: target 777 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +113.08% | $42,303,809.71 |
| DELLSTOCK/USDT:USDT | +34.91% | $8,263,169.27 |
| CTR/USDT:USDT | +32.26% | $1,211,461.22 |
| CLO/USDT:USDT | +22.00% | $1,600,977.07 |
| AIGENSYN/USDT:USDT | +17.54% | $1,195,447.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HBAR/USDT:USDT | below_1h_threshold | +1.01% | +1.10% |
| ALLO/USDT:USDT | below_1h_threshold | +0.91% | +0.99% |
| RIF/USDT:USDT | below_1h_threshold | +0.91% | +0.99% |
| INJ/USDT:USDT | below_1h_threshold | +0.90% | +0.98% |
| XPL/USDT:USDT | below_1h_threshold | +0.73% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
