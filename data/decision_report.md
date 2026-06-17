# Decision Report

- generated_at: 2026-06-17T05:07:21.798624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6904**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6904, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.05% | **+0.02%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/16 | 25.0% | -1.50% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| ASK_LONG | 20/20 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +3.42% | **+2.22%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +2.56% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$195.88** / 初期 $100.00 (+95.88%)
- 確定: 1777件 (Win 478 / Loss 555 / Flat 744) / skip 1688件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $195.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.92** / 初期 $100.00 (-0.08%)
- 確定: 177件 (Win 37 / Loss 33 / Flat 107) / skip 138件
- 成長率目線: 平均log -0.000005 / 幾何平均 -0.000% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0966 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $99.92

## 5. Latest Market Context

- 更新: 2026-06-17T05:07:17.563397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65869.5
- Funnel: target 782 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +29.74% | $10,644,220.01 |
| ESPORTS/USDT:USDT | +27.28% | $3,885,306.77 |
| SPX/USDT:USDT | +22.63% | $7,224,886.75 |
| SQD/USDT:USDT | +21.77% | $1,472,998.88 |
| BTW/USDT:USDT | +21.70% | $3,313,143.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.47% | +3.44% |
| BR/USDT:USDT | below_1h_threshold | +3.14% | +3.11% |
| STG/USDT:USDT | below_1h_threshold | +2.82% | +2.79% |
| TRIA/USDT:USDT | below_1h_threshold | +2.46% | +2.44% |
| SQD/USDT:USDT | below_1h_threshold | +2.36% | +2.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
