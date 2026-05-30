# Decision Report

- generated_at: 2026-05-30T02:44:34.179245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5092**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5092, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.13% | **+0.25%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +5.11% | **+1.53%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.83% | **+1.10%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.43% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 750件 (Win 175 / Loss 226 / Flat 349) / skip 903件
- 成長率目線: 平均log +0.000305 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T02:44:31.620823+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=73690.2
- Funnel: target 773 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +32.80% | $10,149,358.17 |
| XLM/USDT:USDT | +31.34% | $441,349,675.42 |
| LAB/USDT:USDT | +19.13% | $133,653,896.22 |
| OL/USDT:USDT | +18.00% | $1,528,453.37 |
| ALGO/USDT:USDT | +15.79% | $7,947,429.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.03% | +2.94% |
| APE/USDT:USDT | below_1h_threshold | +2.92% | +2.83% |
| XLM/USDT:USDT | below_1h_threshold | +2.79% | +2.70% |
| CTR/USDT:USDT | below_1h_threshold | +2.79% | +2.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.63% | +2.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
