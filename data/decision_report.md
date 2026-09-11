# Decision Report

- generated_at: 2026-09-11T13:11:24.693006+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14220**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=14220, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.58% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.66% | **+1.33%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.19** / 初期 $100.00 (+978.19%)
- 確定: 5382件 (Win 1621 / Loss 1740 / Flat 2021) / skip 5399件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.98% 残高後 $1,078.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4827件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.71** / 初期 $100.00 (+23.71%)
- 確定: 2722件 (Win 805 / Loss 1041 / Flat 876) / pending 6件 / skip 2965件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.71

## 6. Latest Market Context

- 更新: 2026-09-11T13:11:16.273716+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=77590.6
- Funnel: target 1067 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +83.56% | $3,134,971.03 |
| STONK/USDT:USDT | +69.84% | $1,116,498.41 |
| NIULAI/USDT:USDT | +55.72% | $20,368,545.16 |
| RAY/USDT:USDT | +24.74% | $22,534,912.79 |
| MET/USDT:USDT | +19.47% | $1,392,010.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.91% | +4.42% |
| KORU/USDT:USDT | below_1h_threshold | +3.68% | +4.20% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.90% | +3.42% |
| STORJ/USDT:USDT | below_1h_threshold | +2.59% | +3.11% |
| SNXX/USDT:USDT | below_1h_threshold | +2.41% | +2.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
