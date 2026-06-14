# Decision Report

- generated_at: 2026-06-14T13:00:59.013671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6663**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=6663, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$170.38** / 初期 $100.00 (+70.38%)
- 確定: 1536件 (Win 408 / Loss 487 / Flat 641) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $170.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 57件 (Win 19 / Loss 12 / Flat 26) / skip 17件
- 成長率目線: 平均log -0.000176 / 幾何平均 -0.018% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T13:00:54.113238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64315.5
- Funnel: target 770 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +53.64% | $65,634,124.46 |
| BANANAS31/USDT:USDT | +25.90% | $1,239,025.88 |
| TRADOOR/USDT:USDT | +22.96% | $8,204,064.87 |
| OPG/USDT:USDT | +20.56% | $1,549,696.69 |
| MITO/USDT:USDT | +17.33% | $1,050,690.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +0.61% | +0.58% |
| TRADOOR/USDT:USDT | below_1h_threshold | +0.48% | +0.45% |
| MEGA/USDT:USDT | below_1h_threshold | +0.46% | +0.43% |
| OPG/USDT:USDT | below_1h_threshold | +0.44% | +0.41% |
| LAB/USDT:USDT | below_1h_threshold | +0.38% | +0.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
