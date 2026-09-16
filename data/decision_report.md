# Decision Report

- generated_at: 2026-09-16T10:06:16.102098+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14658**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14658, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +2.22% | **+0.93%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.38% | **+0.30%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.86% | **+1.79%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.67% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.41% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,038.92** / 初期 $100.00 (+938.92%)
- 確定: 5536件 (Win 1648 / Loss 1790 / Flat 2098) / skip 5683件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,038.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.53** / 初期 $100.00 (+128.53%)
- 確定: 3064件 (Win 840 / Loss 722 / Flat 1502) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $228.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.85** / 初期 $100.00 (+24.85%)
- 確定: 2947件 (Win 877 / Loss 1157 / Flat 913) / pending 3件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000424 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $124.85

## 6. Latest Market Context

- 更新: 2026-09-16T10:06:05.585212+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75943.0
- Funnel: target 1058 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +112.13% | $15,780,958.16 |
| LSK/USDT:USDT | +25.71% | $20,898,432.08 |
| USELESS/USDT:USDT | +16.34% | $7,131,995.30 |
| BR/USDT:USDT | +12.73% | $15,370,215.99 |
| LONGXIA/USDT:USDT | +12.49% | $2,623,205.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.37% | +2.40% |
| BR/USDT:USDT | below_1h_threshold | +1.60% | +1.62% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.54% | +1.56% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.56% |
| SYN/USDT:USDT | below_1h_threshold | +0.52% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
