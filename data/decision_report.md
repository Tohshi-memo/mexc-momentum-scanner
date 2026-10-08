# Decision Report

- generated_at: 2026-10-08T13:11:27.288094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16334**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=16334, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/8 | 50.0% | +2.28% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.37% | **+0.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.49% | **+0.44%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.69% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_BB3S_LONG | 9/12 | 75.0% | +0.52% | **+0.39%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.18% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6279件 (Win 1845 / Loss 2012 / Flat 2422) / skip 6616件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6113件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4495件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T13:11:15.743472+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=82425.1
- Funnel: target 1082 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +100.45% | $3,589,447.93 |
| MET/USDT:USDT | +38.76% | $32,585,302.59 |
| UAI/USDT:USDT | +16.86% | $3,188,873.84 |
| STRK/USDT:USDT | +16.65% | $6,958,606.34 |
| JUP/USDT:USDT | +13.94% | $44,980,872.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OGN/USDT:USDT | below_1h_threshold | +4.21% | +4.02% |
| AKE/USDT:USDT | below_1h_threshold | +1.44% | +1.26% |
| STRK/USDT:USDT | below_1h_threshold | +1.30% | +1.12% |
| BSPSTOCK/USDT:USDT | below_1h_threshold | +1.13% | +0.94% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
