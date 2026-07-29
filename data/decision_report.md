# Decision Report

- generated_at: 2026-07-29T19:56:32.187571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9830**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.63% / filled 20/20。**
- 全期間 MARKET基準: n=9830, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.63% | **+2.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.63% | **+2.63%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.81% | **+2.39%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.41% | **+0.84%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.29% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.84% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.75% | **-0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.47** / 初期 $100.00 (+20.47%)
- 確定トレード: 163件 (TP 64 / SL 94 / EXP 5)
- 最新: SNXX/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.47
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2872件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 1999件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 540件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T19:56:21.146429+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.30% price=63635.6
- Funnel: target 911 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +19.61% | $4,670,056.21 |
| AEON1/USDT:USDT | +10.62% | $2,493,416.06 |
| DIA/USDT:USDT | +10.35% | $2,141,463.45 |
| LAB/USDT:USDT | +6.59% | $2,135,000.87 |
| RAVE/USDT:USDT | +5.53% | $2,377,945.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EWY/USDT:USDT | below_1h_threshold | +3.98% | +5.27% |
| BESTOCK/USDT:USDT | below_1h_threshold | +3.97% | +5.26% |
| ESP/USDT:USDT | below_1h_threshold | +3.18% | +4.48% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.01% | +4.31% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.95% | +4.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
