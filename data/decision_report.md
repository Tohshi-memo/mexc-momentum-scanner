# Decision Report

- generated_at: 2026-09-04T10:46:51.523541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13610**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=13610, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.91% | **+0.78%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5010件 (Win 1516 / Loss 1644 / Flat 1850) / skip 5161件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.25** / 初期 $100.00 (+85.25%)
- 確定: 2416件 (Win 681 / Loss 577 / Flat 1158) / skip 4605件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $185.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.42** / 初期 $100.00 (+16.42%)
- 確定: 2259件 (Win 668 / Loss 878 / Flat 713) / pending 6件 / skip 2819件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.42

## 6. Latest Market Context

- 更新: 2026-09-04T10:46:31.833733+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=81003.0
- Funnel: target 1052 → liquid 163 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1, 4h RSI 69.2 >= 65=1, 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +49.13% | $7,273,610.41 |
| USELESS/USDT:USDT | +24.72% | $40,372,413.35 |
| BASECAT/USDT:USDT | +22.13% | $2,088,428.05 |
| TRIA/USDT:USDT | +21.77% | $8,534,051.75 |
| HNT/USDT:USDT | +18.42% | $13,707,998.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +2.13% | +2.15% |
| CAKE/USDT:USDT | below_1h_threshold | +1.75% | +1.77% |
| LIT/USDT:USDT | below_1h_threshold | +1.24% | +1.26% |
| XPL/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |
| AKE/USDT:USDT | below_1h_threshold | +0.73% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
