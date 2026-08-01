# Decision Report

- generated_at: 2026-08-01T15:46:17.976560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10100**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10100, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +0.99% | **+0.94%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.31% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.86% | **+3.91%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.07% | **+1.24%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.74% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.82** / 初期 $100.00 (+470.82%)
- 確定: 3638件 (Win 1158 / Loss 1191 / Flat 1289) / skip 3023件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $570.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2232件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.16** / 初期 $100.00 (+11.16%)
- 確定: 911件 (Win 288 / Loss 356 / Flat 267) / pending 3件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $111.16

## 6. Latest Market Context

- 更新: 2026-08-01T15:46:10.861993+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63024.2
- Funnel: target 922 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +47.30% | $1,439,855.95 |
| BTW/USDT:USDT | +32.82% | $12,989,413.26 |
| JIMOTHY/USDT:USDT | +27.98% | $1,515,529.34 |
| EPIC/USDT:USDT | +26.60% | $2,046,323.13 |
| EUL/USDT:USDT | +19.48% | $1,556,439.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.81% | +4.92% |
| SHIB/USDT:USDT | below_1h_threshold | +2.24% | +2.36% |
| EUL/USDT:USDT | below_1h_threshold | +1.99% | +2.10% |
| BTW/USDT:USDT | below_1h_threshold | +1.14% | +1.26% |
| ALLO/USDT:USDT | below_1h_threshold | +0.99% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
