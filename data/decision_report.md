# Decision Report

- generated_at: 2026-09-11T11:41:22.310021+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14215**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=14215, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.30% | **-0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.61% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.52% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.81% | **+0.38%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,073.12** / 初期 $100.00 (+973.12%)
- 確定: 5380件 (Win 1620 / Loss 1739 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.52% 残高後 $1,073.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4822件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.86** / 初期 $100.00 (+22.86%)
- 確定: 2718件 (Win 802 / Loss 1040 / Flat 876) / pending 4件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.86

## 6. Latest Market Context

- 更新: 2026-09-11T11:41:10.101579+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=76849.1
- Funnel: target 1068 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +66.70% | $1,387,115.94 |
| NIULAI/USDT:USDT | +51.22% | $18,568,719.04 |
| RAY/USDT:USDT | +21.52% | $20,183,068.22 |
| CNPY/USDT:USDT | +18.27% | $2,789,342.29 |
| LSK/USDT:USDT | +16.36% | $2,340,241.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.07% | +3.21% |
| RAY/USDT:USDT | below_1h_threshold | +1.53% | +1.67% |
| VVV/USDT:USDT | below_1h_threshold | +1.50% | +1.65% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.43% | +1.57% |
| NES/USDT:USDT | below_1h_threshold | +0.98% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
