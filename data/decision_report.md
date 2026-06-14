# Decision Report

- generated_at: 2026-06-14T10:27:41.537038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6658**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6658, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_ATR | 8/20 | 40.0% | +0.10% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.65% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.23** / 初期 $100.00 (+71.23%)
- 確定: 1531件 (Win 408 / Loss 486 / Flat 637) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEGA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $171.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 57件 (Win 19 / Loss 12 / Flat 26) / skip 12件
- 成長率目線: 平均log -0.000176 / 幾何平均 -0.018% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T10:27:36.868859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64571.6
- Funnel: target 770 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +111.81% | $50,314,061.15 |
| VELVET/USDT:USDT | +18.24% | $64,978,893.14 |
| TRADOOR/USDT:USDT | +13.61% | $7,841,783.45 |
| BTW/USDT:USDT | +12.75% | $3,321,496.72 |
| BILL/USDT:USDT | +10.60% | $2,067,835.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.74% | +3.76% |
| H/USDT:USDT | below_1h_threshold | +2.38% | +2.40% |
| PLAY/USDT:USDT | below_1h_threshold | +1.85% | +1.87% |
| CHIP/USDT:USDT | below_1h_threshold | +1.41% | +1.43% |
| BRETT/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
