# Decision Report

- generated_at: 2026-06-17T06:10:30.166460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6910**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6910, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.73% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK_LONG | 20/20 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.49% | **+1.62%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +2.73% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.85** / 初期 $100.00 (+96.85%)
- 確定: 1783件 (Win 481 / Loss 557 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $196.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定: 183件 (Win 40 / Loss 35 / Flat 108) / skip 138件
- 成長率目線: 平均log +0.000027 / 幾何平均 +0.003% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0935 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $100.50

## 5. Latest Market Context

- 更新: 2026-06-17T06:10:21.820089+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65815.0
- Funnel: target 785 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +31.43% | $11,680,697.50 |
| SQD/USDT:USDT | +28.03% | $1,742,073.44 |
| SPX/USDT:USDT | +24.15% | $7,291,953.66 |
| ESPORTS/USDT:USDT | +22.02% | $4,039,129.10 |
| UNI/USDT:USDT | +18.17% | $45,524,283.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +1.99% | +1.96% |
| UNI/USDT:USDT | below_1h_threshold | +1.88% | +1.86% |
| SQD/USDT:USDT | below_1h_threshold | +1.04% | +1.01% |
| GRASS/USDT:USDT | below_1h_threshold | +0.76% | +0.73% |
| LIT/USDT:USDT | below_1h_threshold | +0.75% | +0.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
