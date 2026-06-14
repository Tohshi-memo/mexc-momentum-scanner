# Decision Report

- generated_at: 2026-06-14T13:53:15.189568+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6664**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=6664, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| ASK | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.62% | **+0.49%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 2/18 | 11.1% | +1.61% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.28% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$170.38** / 初期 $100.00 (+70.38%)
- 確定: 1537件 (Win 408 / Loss 487 / Flat 642) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $170.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 58件 (Win 19 / Loss 12 / Flat 27) / skip 17件
- 成長率目線: 平均log -0.000173 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T13:53:10.493674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64283.0
- Funnel: target 770 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +27.65% | $1,061,759.33 |
| ZKC/USDT:USDT | +26.44% | $1,327,977.28 |
| TRADOOR/USDT:USDT | +25.50% | $8,347,249.65 |
| OPG/USDT:USDT | +24.32% | $1,700,118.40 |
| BANANAS31/USDT:USDT | +20.72% | $1,446,253.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.37% | +4.40% |
| CLO/USDT:USDT | below_1h_threshold | +4.11% | +4.13% |
| CHIP/USDT:USDT | below_1h_threshold | +3.66% | +3.68% |
| OPG/USDT:USDT | below_1h_threshold | +3.57% | +3.59% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.55% | +2.58% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
