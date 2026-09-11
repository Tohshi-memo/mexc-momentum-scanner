# Decision Report

- generated_at: 2026-09-11T11:16:21.473566+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14211**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14211, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.36% | **+0.41%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.27% | **-0.18%** |
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |
| LIMIT_BB3S | 3/16 | 18.8% | -2.96% | **-0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.27% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.92% | **+0.55%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.81% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,069.39** / 初期 $100.00 (+969.39%)
- 確定: 5376件 (Win 1618 / Loss 1737 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,069.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2803件 (Win 770 / Loss 650 / Flat 1383) / skip 4819件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.97** / 初期 $100.00 (+22.97%)
- 確定: 2714件 (Win 801 / Loss 1038 / Flat 875) / pending 5件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000153 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.97

## 6. Latest Market Context

- 更新: 2026-09-11T11:16:09.215519+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=76734.4
- Funnel: target 1068 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +64.10% | $17,341,435.46 |
| LAB/USDT:USDT | +32.22% | $1,830,277.71 |
| LSK/USDT:USDT | +21.42% | $2,144,958.30 |
| RAY/USDT:USDT | +18.90% | $19,842,443.99 |
| CNPY/USDT:USDT | +18.71% | $2,785,323.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +1.69% | +1.98% |
| BTR/USDT:USDT | below_1h_threshold | +0.85% | +1.15% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.43% | +0.73% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.35% | +0.64% |
| 4/USDT:USDT | below_1h_threshold | +0.26% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
