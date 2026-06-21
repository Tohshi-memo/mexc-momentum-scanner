# Decision Report

- generated_at: 2026-06-21T18:08:00.083942+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.12% / filled 20/20。**
- 全期間 MARKET基準: n=7321, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |
| ASK | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.92% | **+1.73%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.29% | **+0.34%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.14% | **+0.29%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.03% | **+0.01%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.01% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2031件 (Win 599 / Loss 668 / Flat 764) / skip 1851件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 421件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T18:07:54.669962+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=63996.9
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STO/USDT:USDT | +14.12% | $3,145,473.94 |
| RESOLV/USDT:USDT | +6.39% | $13,975,579.67 |
| UB/USDT:USDT | +5.28% | $4,397,945.30 |
| SLX/USDT:USDT | +5.07% | $1,011,709.50 |
| UAI/USDT:USDT | +4.97% | $1,538,013.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.25% | +2.44% |
| BEAT/USDT:USDT | below_1h_threshold | +0.99% | +1.18% |
| UAI/USDT:USDT | below_1h_threshold | +0.91% | +1.10% |
| SYN/USDT:USDT | below_1h_threshold | +0.69% | +0.88% |
| UB/USDT:USDT | below_1h_threshold | +0.68% | +0.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
