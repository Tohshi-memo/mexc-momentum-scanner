# Decision Report

- generated_at: 2026-06-21T18:20:58.802618+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7322**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.39% / filled 20/20。**
- 全期間 MARKET基準: n=7322, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.17% | **+1.95%** |
| ASK | 20/20 | 100.0% | +1.76% | **+1.76%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.85% | **+1.30%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.29% | **+0.34%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.13% | **+0.34%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.01% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2031件 (Win 599 / Loss 668 / Flat 764) / skip 1852件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 422件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T18:20:54.359167+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=63985.4
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STO/USDT:USDT | +14.99% | $3,410,341.57 |
| UAI/USDT:USDT | +7.44% | $1,587,730.58 |
| UB/USDT:USDT | +7.11% | $4,550,747.99 |
| RESOLV/USDT:USDT | +6.73% | $14,380,824.43 |
| SLX/USDT:USDT | +5.67% | $1,014,382.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.78% | +4.99% |
| UAI/USDT:USDT | below_1h_threshold | +3.38% | +3.59% |
| UB/USDT:USDT | below_1h_threshold | +2.43% | +2.63% |
| BSB/USDT:USDT | below_1h_threshold | +1.97% | +2.18% |
| RIVER/USDT:USDT | below_1h_threshold | +1.74% | +1.95% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
