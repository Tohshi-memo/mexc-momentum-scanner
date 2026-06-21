# Decision Report

- generated_at: 2026-06-21T11:30:46.135428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7302**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=7302, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.44% | **+0.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.18% | **+0.14%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2030件 (Win 599 / Loss 668 / Flat 763) / skip 1833件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 402件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T11:30:41.685441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64370.0
- Funnel: target 796 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +73.32% | $9,880,753.55 |
| LAB/USDT:USDT | +25.08% | $26,852,506.90 |
| BULLA/USDT:USDT | +24.13% | $1,352,706.58 |
| UB/USDT:USDT | +21.13% | $1,670,098.30 |
| BICO/USDT:USDT | +20.81% | $52,455,620.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TNSR/USDT:USDT | below_1h_threshold | +3.13% | +3.08% |
| LAB/USDT:USDT | below_1h_threshold | +2.07% | +2.02% |
| UB/USDT:USDT | below_1h_threshold | +1.93% | +1.88% |
| W/USDT:USDT | below_1h_threshold | +1.35% | +1.30% |
| AERO/USDT:USDT | below_1h_threshold | +0.80% | +0.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
