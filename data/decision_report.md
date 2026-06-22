# Decision Report

- generated_at: 2026-06-22T07:17:39.455276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7353**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7353, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.16% | **+1.52%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2032件 (Win 599 / Loss 668 / Flat 765) / skip 1882件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 453件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T07:17:34.915657+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=64197.6
- Funnel: target 801 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +46.27% | $5,839,318.12 |
| UB/USDT:USDT | +33.44% | $10,919,594.69 |
| CLO/USDT:USDT | +27.49% | $3,682,220.84 |
| ZEST/USDT:USDT | +24.46% | $1,927,440.74 |
| O/USDT:USDT | +19.19% | $1,871,671.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.93% | +4.55% |
| SYN/USDT:USDT | below_1h_threshold | +3.32% | +2.95% |
| ALLO/USDT:USDT | below_1h_threshold | +2.53% | +2.16% |
| ID/USDT:USDT | below_1h_threshold | +2.20% | +1.83% |
| TIA/USDT:USDT | below_1h_threshold | +1.62% | +1.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
