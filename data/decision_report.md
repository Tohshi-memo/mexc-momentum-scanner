# Decision Report

- generated_at: 2026-06-14T01:35:42.585583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6627**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=6627, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.98% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.51% | **+0.26%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.14% | **+0.09%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.06% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.69** / 初期 $100.00 (+67.69%)
- 確定: 1500件 (Win 403 / Loss 480 / Flat 617) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $167.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 38件 (Win 13 / Loss 11 / Flat 14) / skip 0件
- 成長率目線: 平均log -0.000304 / 幾何平均 -0.030% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-14T01:35:38.416709+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64566.1
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +29.10% | $19,280,802.95 |
| TRADOOR/USDT:USDT | +27.83% | $3,052,091.96 |
| MEGA/USDT:USDT | +14.64% | $3,475,349.88 |
| RIF/USDT:USDT | +11.63% | $13,760,846.92 |
| BTW/USDT:USDT | +11.52% | $1,988,922.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.40% | +4.33% |
| SIREN/USDT:USDT | below_1h_threshold | +3.92% | +3.84% |
| JASMY/USDT:USDT | below_1h_threshold | +1.83% | +1.75% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.70% | +1.62% |
| AT/USDT:USDT | below_1h_threshold | +1.01% | +0.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
