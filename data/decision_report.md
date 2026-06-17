# Decision Report

- generated_at: 2026-06-17T10:38:54.278776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6925**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6925, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +2.37% | **+1.42%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.69% | **+1.35%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$194.84** / 初期 $100.00 (+94.84%)
- 確定: 1798件 (Win 487 / Loss 566 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $194.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.60** / 初期 $100.00 (+0.60%)
- 確定: 198件 (Win 45 / Loss 43 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000030 / 幾何平均 +0.003% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $100.60

## 5. Latest Market Context

- 更新: 2026-06-17T10:38:49.187492+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64895.7
- Funnel: target 785 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +51.26% | $6,504,556.64 |
| HIGH/USDT:USDT | +40.43% | $2,957,883.42 |
| ID/USDT:USDT | +24.53% | $1,287,292.79 |
| SQD/USDT:USDT | +23.00% | $2,852,967.26 |
| UNI/USDT:USDT | +20.45% | $58,243,096.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.40% | +4.37% |
| ID/USDT:USDT | below_1h_threshold | +2.01% | +1.99% |
| AERO/USDT:USDT | below_1h_threshold | +1.74% | +1.72% |
| LDO/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |
| SPX/USDT:USDT | below_1h_threshold | +1.16% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
