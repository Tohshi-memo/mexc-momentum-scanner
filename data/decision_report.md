# Decision Report

- generated_at: 2026-06-17T13:09:22.634880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6939**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=6939, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.35% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.62% | **+0.55%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.92% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_BB3S_LONG | 5/11 | 45.5% | +0.45% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.03** / 初期 $100.00 (+97.03%)
- 確定: 1811件 (Win 493 / Loss 571 / Flat 747) / skip 1689件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $197.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.90** / 初期 $100.00 (+1.90%)
- 確定: 212件 (Win 52 / Loss 48 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $101.90

## 5. Latest Market Context

- 更新: 2026-06-17T13:09:17.311361+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64960.4
- Funnel: target 790 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +69.56% | $1,818,062.41 |
| ESPORTS/USDT:USDT | +56.41% | $11,006,926.23 |
| BP/USDT:USDT | +27.59% | $1,073,583.97 |
| HIGH/USDT:USDT | +27.38% | $3,573,869.87 |
| XPL/USDT:USDT | +24.82% | $8,043,577.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +2.13% | +2.20% |
| STG/USDT:USDT | below_1h_threshold | +1.41% | +1.49% |
| LIT/USDT:USDT | below_1h_threshold | +0.80% | +0.87% |
| COAI/USDT:USDT | below_1h_threshold | +0.68% | +0.75% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +0.46% | +0.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
