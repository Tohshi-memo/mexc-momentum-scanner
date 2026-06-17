# Decision Report

- generated_at: 2026-06-17T09:52:10.514753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6922**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6922, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +4.78% | **+2.66%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.64% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.06% | **+1.07%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.80** / 初期 $100.00 (+97.80%)
- 確定: 1795件 (Win 487 / Loss 563 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $197.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.67** / 初期 $100.00 (+1.67%)
- 確定: 195件 (Win 45 / Loss 40 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000085 / 幾何平均 +0.008% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1281 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.67

## 5. Latest Market Context

- 更新: 2026-06-17T09:52:04.907804+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64880.3
- Funnel: target 784 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.3 >= 65=1, 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HIGH/USDT:USDT | +43.75% | $2,428,637.85 |
| ESPORTS/USDT:USDT | +41.47% | $6,128,253.24 |
| SQD/USDT:USDT | +24.09% | $2,721,899.58 |
| ID/USDT:USDT | +21.26% | $1,243,558.72 |
| UNI/USDT:USDT | +20.12% | $57,139,826.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +4.28% | +4.30% |
| TRIA/USDT:USDT | below_1h_threshold | +4.22% | +4.23% |
| STG/USDT:USDT | below_1h_threshold | +2.32% | +2.34% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.29% | +2.30% |
| USELESS/USDT:USDT | below_1h_threshold | +2.22% | +2.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
