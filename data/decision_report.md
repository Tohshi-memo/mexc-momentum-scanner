# Decision Report

- generated_at: 2026-06-14T14:06:23.293081+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6666**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=6666, expectancy=-0.05%
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
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.12% | **+0.09%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.26% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.00** / 初期 $100.00 (+1.00%)
- 確定トレード: 1件 (TP 1 / SL 0 / EXP 0)
- 最新: BANANAS31/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$170.38** / 初期 $100.00 (+70.38%)
- 確定: 1539件 (Win 408 / Loss 487 / Flat 644) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $170.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 58件 (Win 19 / Loss 12 / Flat 27) / skip 19件
- 成長率目線: 平均log -0.000173 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T14:06:15.114395+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64292.4
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZKC/USDT:USDT | +30.04% | $1,416,015.33 |
| CLO/USDT:USDT | +28.72% | $1,067,285.74 |
| TRADOOR/USDT:USDT | +26.40% | $8,394,574.99 |
| OPG/USDT:USDT | +24.44% | $1,668,411.14 |
| BANANAS31/USDT:USDT | +21.09% | $1,452,357.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZKC/USDT:USDT | below_1h_threshold | +3.30% | +3.28% |
| JCT/USDT:USDT | below_1h_threshold | +3.13% | +3.11% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.62% | +1.60% |
| JASMY/USDT:USDT | below_1h_threshold | +1.31% | +1.30% |
| LAB/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
