# Decision Report

- generated_at: 2026-06-20T05:55:44.552860+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7209**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=7209, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/16 | 12.5% | +6.74% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| ASK | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.61% | **+0.58%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.50% | **+0.17%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.05% | **-0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.16% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.84** / 初期 $100.00 (+124.84%)
- 確定: 1970件 (Win 571 / Loss 641 / Flat 758) / skip 1800件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $224.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 310件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T05:55:39.529505+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63647.0
- Funnel: target 795 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 78.2 >= 65=1, 4h RSI 69.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +53.64% | $18,977,352.33 |
| BICO/USDT:USDT | +37.20% | $21,043,724.28 |
| BLESS/USDT:USDT | +28.63% | $6,057,338.33 |
| AXS/USDT:USDT | +20.00% | $3,816,347.85 |
| EIGEN/USDT:USDT | +19.98% | $6,869,489.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_relative_strength | +5.13% | +4.98% |
| CLO/USDT:USDT | below_1h_threshold | +4.82% | +4.67% |
| BLESS/USDT:USDT | below_1h_threshold | +1.64% | +1.49% |
| VVV/USDT:USDT | below_1h_threshold | +1.58% | +1.43% |
| BSB/USDT:USDT | below_1h_threshold | +1.49% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
