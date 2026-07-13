# Decision Report

- generated_at: 2026-07-13T06:41:16.131403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8623**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.57% / filled 20/20。**
- 全期間 MARKET基準: n=8623, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.24% | **+0.44%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.67% | **+1.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.43% | **+0.35%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.25% | **+0.25%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.10% | **+0.08%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.04% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2793件 (Win 876 / Loss 923 / Flat 994) / skip 2391件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1389件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.68** / 初期 $100.00 (-0.32%)
- 確定: 29件 (Win 11 / Loss 18 / Flat 0) / pending 2件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000604 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLAST/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.68

## 6. Latest Market Context

- 更新: 2026-07-13T06:41:09.773625+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=62775.7
- Funnel: target 863 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XEC/USDT:USDT | +35.82% | $1,678,953.64 |
| DODO/USDT:USDT | +27.54% | $6,570,595.36 |
| KITE/USDT:USDT | +12.23% | $1,150,118.09 |
| BLAST/USDT:USDT | +10.06% | $2,699,666.18 |
| ANSEM/USDT:USDT | +6.65% | $4,728,931.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +1.69% | +1.67% |
| PYTH/USDT:USDT | below_1h_threshold | +1.28% | +1.27% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.80% | +0.78% |
| RIVER/USDT:USDT | below_1h_threshold | +0.77% | +0.75% |
| EDGE/USDT:USDT | below_1h_threshold | +0.55% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
