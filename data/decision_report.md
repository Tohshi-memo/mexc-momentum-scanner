# Decision Report

- generated_at: 2026-08-28T13:06:20.242393+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12873**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=12873, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_BB3S | 5/19 | 26.3% | +4.34% | **+1.14%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.20% | **+1.02%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.30% | **-0.17%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.57% | **-0.29%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.29% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.45** / 初期 $100.00 (+612.45%)
- 確定: 4676件 (Win 1414 / Loss 1533 / Flat 1729) / skip 4758件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $712.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4281件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.98** / 初期 $100.00 (+14.98%)
- 確定: 1990件 (Win 581 / Loss 763 / Flat 646) / pending 0件 / skip 2354件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000612 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $114.98

## 6. Latest Market Context

- 更新: 2026-08-28T13:06:11.187262+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79421.0
- Funnel: target 1023 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +88.21% | $1,774,233.76 |
| HEMI/USDT:USDT | +41.88% | $5,822,191.07 |
| LIGHT/USDT:USDT | +26.64% | $4,800,353.33 |
| MAGMA/USDT:USDT | +22.22% | $4,372,392.23 |
| EDEN/USDT:USDT | +17.77% | $4,071,947.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +2.38% | +2.34% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.97% | +1.92% |
| KORU/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| MUU/USDT:USDT | below_1h_threshold | +1.27% | +1.23% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
