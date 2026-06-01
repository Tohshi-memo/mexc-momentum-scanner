# Decision Report

- generated_at: 2026-06-01T00:25:31.121014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5243**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5243, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.60% | **+1.08%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.14% | **-0.14%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.32% | **-0.16%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.53% | **+1.93%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.71% | **+1.54%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.50% | **+1.43%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.58% | **+1.42%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.12% | **+1.38%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.88** / 初期 $100.00 (+33.88%)
- 確定: 878件 (Win 205 / Loss 261 / Flat 412) / skip 926件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IBMSTOCK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $133.88

## 4. Latest Market Context

- 更新: 2026-06-01T00:25:28.319689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73770.1
- Funnel: target 774 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.8 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +112.17% | $20,606,294.71 |
| STG/USDT:USDT | +33.57% | $21,233,049.85 |
| H/USDT:USDT | +20.08% | $12,960,203.81 |
| ZORA/USDT:USDT | +19.64% | $1,731,125.36 |
| CTR/USDT:USDT | +16.56% | $1,375,513.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTR/USDT:USDT | below_1h_threshold | +3.92% | +3.76% |
| WLD/USDT:USDT | below_1h_threshold | +3.06% | +2.90% |
| PLAY/USDT:USDT | below_1h_threshold | +2.79% | +2.64% |
| RENDER/USDT:USDT | below_1h_threshold | +2.25% | +2.09% |
| ORDI/USDT:USDT | below_1h_threshold | +2.12% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
