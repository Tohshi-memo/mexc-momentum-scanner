# Decision Report

- generated_at: 2026-07-03T12:07:38.832772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8158**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=8158, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.03% | **-0.03%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.55% | **-0.25%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.66% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.46** / 初期 $100.00 (+189.46%)
- 確定: 2479件 (Win 763 / Loss 826 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $289.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.39** / 初期 $100.00 (+6.39%)
- 確定: 604件 (Win 145 / Loss 143 / Flat 316) / skip 965件
- 成長率目線: 平均log +0.000102 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $106.39

## 5. Latest Market Context

- 更新: 2026-07-03T12:07:32.884919+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=62115.7
- Funnel: target 834 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARPA/USDT:USDT | +52.80% | $4,203,405.73 |
| NEX/USDT:USDT | +50.89% | $2,693,359.01 |
| RIF/USDT:USDT | +44.45% | $8,621,745.13 |
| ZKP/USDT:USDT | +28.41% | $5,178,734.04 |
| THE/USDT:USDT | +23.84% | $2,927,613.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.01% | +2.81% |
| TIA/USDT:USDT | below_1h_threshold | +1.21% | +1.01% |
| GRASS/USDT:USDT | below_1h_threshold | +1.20% | +1.00% |
| RIVER/USDT:USDT | below_1h_threshold | +1.19% | +0.99% |
| XPL/USDT:USDT | below_1h_threshold | +0.78% | +0.58% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
