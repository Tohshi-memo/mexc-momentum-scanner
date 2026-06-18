# Decision Report

- generated_at: 2026-06-18T22:56:44.676265+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7084**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7084, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.86% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |
| ASK | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.71% | **+1.19%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.40% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$103.51** / 初期 $100.00 (+3.51%)
- 確定トレード: 17件 (TP 8 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.30** / 初期 $100.00 (+123.30%)
- 確定: 1904件 (Win 542 / Loss 610 / Flat 752) / skip 1741件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASED/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $223.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 187件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T22:56:40.363991+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=62836.1
- Funnel: target 795 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +104.77% | $3,342,089.54 |
| ZEREBRO/USDT:USDT | +20.31% | $2,811,443.19 |
| BASED/USDT:USDT | +17.58% | $2,519,644.70 |
| SYN/USDT:USDT | +16.80% | $18,556,316.35 |
| EDEN/USDT:USDT | +16.55% | $1,909,485.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +2.15% | +2.32% |
| RIVER/USDT:USDT | below_1h_threshold | +2.09% | +2.25% |
| PLAY/USDT:USDT | below_1h_threshold | +0.96% | +1.12% |
| LIT/USDT:USDT | below_1h_threshold | +0.86% | +1.02% |
| CHIP/USDT:USDT | below_1h_threshold | +0.85% | +1.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
