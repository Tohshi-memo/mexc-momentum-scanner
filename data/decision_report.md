# Decision Report

- generated_at: 2026-05-30T08:04:50.331488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5110**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5110, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.76% | **+1.76%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.89% | **+1.04%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.95%** |
| ASK_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.17** / 初期 $100.00 (+26.17%)
- 確定: 765件 (Win 178 / Loss 229 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $126.17

## 4. Latest Market Context

- 更新: 2026-05-30T08:04:48.110487+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73510.0
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +58.20% | $14,264,254.85 |
| LAB/USDT:USDT | +21.83% | $120,328,627.70 |
| XLM/USDT:USDT | +18.14% | $435,303,557.73 |
| OL/USDT:USDT | +12.49% | $1,444,687.75 |
| ALGO/USDT:USDT | +9.61% | $7,683,245.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +1.12% | +1.12% |
| HEI/USDT:USDT | below_1h_threshold | +1.06% | +1.07% |
| H/USDT:USDT | below_1h_threshold | +0.47% | +0.47% |
| XLM/USDT:USDT | below_1h_threshold | +0.46% | +0.47% |
| HBAR/USDT:USDT | below_1h_threshold | +0.43% | +0.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
