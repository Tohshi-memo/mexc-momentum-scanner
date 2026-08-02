# Decision Report

- generated_at: 2026-08-02T14:41:22.659138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10166**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=10166, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.72% | **+1.41%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.28% | **+1.22%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_BB3S | 3/19 | 15.8% | +3.73% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3053件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2296件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.61** / 初期 $100.00 (+12.61%)
- 確定: 967件 (Win 307 / Loss 378 / Flat 282) / pending 2件 / skip 667件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $112.61

## 6. Latest Market Context

- 更新: 2026-08-02T14:41:14.994938+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63110.1
- Funnel: target 922 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1, 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +72.51% | $24,040,226.59 |
| HOME/USDT:USDT | +44.52% | $5,052,129.88 |
| UAI/USDT:USDT | +30.35% | $27,820,325.99 |
| MANTRA/USDT:USDT | +21.66% | $1,983,755.74 |
| HYPER/USDT:USDT | +18.06% | $1,826,585.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.45% | +3.43% |
| ROSE/USDT:USDT | below_1h_threshold | +3.35% | +3.32% |
| ADA/USDT:USDT | below_1h_threshold | +1.66% | +1.63% |
| MANTRA/USDT:USDT | below_1h_threshold | +1.62% | +1.60% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.51% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
