# Decision Report

- generated_at: 2026-07-30T10:31:11.606290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9876**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.54% / filled 20/20。**
- 全期間 MARKET基準: n=9876, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.54% | **+3.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.54% | **+3.54%** |
| LIMIT_1PCT | 15/20 | 75.0% | +3.22% | **+2.41%** |
| LIMIT_2PCT | 11/20 | 55.0% | +3.21% | **+1.77%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_3PCT | 7/20 | 35.0% | +2.14% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.19% | **+0.16%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.75% | **-0.19%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.27% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 171件 (TP 67 / SL 99 / EXP 5)
- 最新: AMZU/USDT:USDT SL_HIT PnL -2.81% 残高後 $121.53
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2918件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2045件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.83** / 初期 $100.00 (+11.83%)
- 確定: 781件 (Win 256 / Loss 302 / Flat 223) / pending 1件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.001017 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESP/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.83

## 6. Latest Market Context

- 更新: 2026-07-30T10:31:04.565016+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64600.7
- Funnel: target 916 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +34.31% | $1,118,055.42 |
| ESP/USDT:USDT | +33.30% | $3,436,285.29 |
| MMT/USDT:USDT | +19.17% | $1,302,111.59 |
| MSFU/USDT:USDT | +15.29% | $2,915,727.56 |
| ADVANTESTSTOCK/USDT:USDT | +10.84% | $1,270,903.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESP/USDT:USDT | below_1h_threshold | +4.34% | +4.26% |
| SNXX/USDT:USDT | below_1h_threshold | +3.12% | +3.05% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.14% |
| CAP/USDT:USDT | below_1h_threshold | +1.62% | +1.54% |
| LAB/USDT:USDT | below_1h_threshold | +1.45% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
