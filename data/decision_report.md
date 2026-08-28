# Decision Report

- generated_at: 2026-08-28T14:56:22.438674+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12875**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=12875, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.02% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.54% | **+0.35%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.51% | **+0.28%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.11% | **+0.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.45** / 初期 $100.00 (+612.45%)
- 確定: 4676件 (Win 1414 / Loss 1533 / Flat 1729) / skip 4760件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $712.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4283件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.98** / 初期 $100.00 (+14.98%)
- 確定: 1990件 (Win 581 / Loss 763 / Flat 646) / pending 0件 / skip 2355件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000489 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $114.98

## 6. Latest Market Context

- 更新: 2026-08-28T14:56:13.137244+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=79470.0
- Funnel: target 1023 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +93.85% | $2,179,552.09 |
| HEMI/USDT:USDT | +46.68% | $6,593,664.14 |
| LIGHT/USDT:USDT | +28.73% | $5,721,759.08 |
| MAGMA/USDT:USDT | +24.03% | $4,376,946.87 |
| UB/USDT:USDT | +15.40% | $1,064,085.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +4.64% | +4.45% |
| LONGXIA/USDT:USDT | below_1h_threshold | +4.35% | +4.16% |
| CHIP/USDT:USDT | below_1h_threshold | +4.31% | +4.12% |
| SNXX/USDT:USDT | below_1h_threshold | +4.18% | +3.99% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.59% | +3.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
