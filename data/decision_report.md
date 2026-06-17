# Decision Report

- generated_at: 2026-06-17T12:38:14.485082+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6935**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=6935, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.21% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.83% | **+1.41%** |
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +2.21% | **+1.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.53% | **+0.45%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.02** / 初期 $100.00 (+98.02%)
- 確定: 1807件 (Win 492 / Loss 569 / Flat 746) / skip 1689件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $198.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.74** / 初期 $100.00 (+1.74%)
- 確定: 208件 (Win 50 / Loss 46 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0954 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $101.74

## 5. Latest Market Context

- 更新: 2026-06-17T12:38:05.105655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64792.8
- Funnel: target 790 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.2 >= 65=1, 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +60.57% | $1,373,083.93 |
| ESPORTS/USDT:USDT | +58.25% | $10,227,004.19 |
| HIGH/USDT:USDT | +26.26% | $3,493,815.66 |
| BP/USDT:USDT | +24.04% | $1,061,391.26 |
| BLESS/USDT:USDT | +21.28% | $15,921,029.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +3.54% | +3.51% |
| SIREN/USDT:USDT | below_1h_threshold | +3.11% | +3.08% |
| BP/USDT:USDT | below_1h_threshold | +2.71% | +2.68% |
| JASMY/USDT:USDT | below_1h_threshold | +2.04% | +2.01% |
| GRASS/USDT:USDT | below_1h_threshold | +1.85% | +1.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
