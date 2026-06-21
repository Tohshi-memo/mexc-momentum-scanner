# Decision Report

- generated_at: 2026-06-21T22:39:56.038523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7331**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=7331, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.37% | **+1.24%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.49% | **+1.19%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.39% | **+1.05%** |
| ASK | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.46% | **+0.42%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.14% | **+0.29%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.33% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2031件 (Win 599 / Loss 668 / Flat 764) / skip 1861件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 431件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T22:39:51.554467+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63605.1
- Funnel: target 796 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NAORIS/USDT:USDT | +24.40% | $2,151,664.63 |
| SYN/USDT:USDT | +17.38% | $2,642,482.87 |
| EVAA/USDT:USDT | +13.06% | $1,138,906.39 |
| STO/USDT:USDT | +9.37% | $4,901,770.36 |
| UAI/USDT:USDT | +7.79% | $2,307,813.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.85% | +5.12% |
| SYN/USDT:USDT | below_1h_threshold | +4.23% | +4.50% |
| TNSR/USDT:USDT | below_1h_threshold | +2.72% | +2.99% |
| EVAA/USDT:USDT | below_1h_threshold | +2.66% | +2.93% |
| O/USDT:USDT | below_1h_threshold | +2.58% | +2.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
