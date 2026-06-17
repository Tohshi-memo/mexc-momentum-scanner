# Decision Report

- generated_at: 2026-06-17T13:22:54.898282+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6942**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=6942, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.07% | **+0.59%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.45% | **+0.28%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1690件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.98** / 初期 $100.00 (+1.98%)
- 確定: 215件 (Win 53 / Loss 49 / Flat 113) / skip 138件
- 成長率目線: 平均log +0.000091 / 幾何平均 +0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0872 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $101.98

## 5. Latest Market Context

- 更新: 2026-06-17T13:22:48.690281+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64963.3
- Funnel: target 790 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +70.31% | $1,979,773.15 |
| ESPORTS/USDT:USDT | +54.37% | $11,212,450.23 |
| BP/USDT:USDT | +27.03% | $1,077,586.21 |
| XPL/USDT:USDT | +24.49% | $9,198,510.14 |
| HIGH/USDT:USDT | +22.84% | $3,664,018.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.66% | +4.72% |
| COAI/USDT:USDT | below_1h_threshold | +3.64% | +3.71% |
| BP/USDT:USDT | below_1h_threshold | +1.79% | +1.86% |
| PLAY/USDT:USDT | below_1h_threshold | +0.81% | +0.87% |
| STG/USDT:USDT | below_1h_threshold | +0.79% | +0.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
