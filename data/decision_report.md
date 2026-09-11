# Decision Report

- generated_at: 2026-09-11T11:26:17.288373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14213**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=14213, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.36% | **+0.41%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.30% | **-0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.63% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.11% | **+0.55%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.52% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.81% | **+0.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.44% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,058.72** / 初期 $100.00 (+958.72%)
- 確定: 5378件 (Win 1618 / Loss 1739 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,058.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4820件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.54** / 初期 $100.00 (+22.54%)
- 確定: 2716件 (Win 801 / Loss 1040 / Flat 875) / pending 4件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000127 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.54

## 6. Latest Market Context

- 更新: 2026-09-11T11:26:05.512115+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=76855.8
- Funnel: target 1068 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +53.21% | $1,075,142.00 |
| NIULAI/USDT:USDT | +49.14% | $18,020,799.02 |
| LAB/USDT:USDT | +20.95% | $2,096,911.61 |
| RAY/USDT:USDT | +19.51% | $19,934,873.28 |
| LSK/USDT:USDT | +18.90% | $2,230,995.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +1.42% | +1.55% |
| VVV/USDT:USDT | below_1h_threshold | +1.23% | +1.37% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.15% | +1.28% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.11% | +1.24% |
| BTR/USDT:USDT | below_1h_threshold | +0.99% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
