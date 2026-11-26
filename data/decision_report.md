# Decision Report

- generated_at: 2026-11-26T08:31:24.244489+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19677**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.58% / filled 20/20。**
- 全期間 MARKET基準: n=19677, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.45% | **+2.33%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.11% | **+1.47%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.87% | **+1.31%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.29% | **+0.17%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.32% | **+0.05%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 289件 (TP 105 / SL 176 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,978.32** / 初期 $100.00 (+1878.32%)
- 確定: 7615件 (Win 2192 / Loss 2452 / Flat 2971) / skip 8623件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANTRA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,978.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7867件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7840件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000057 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T08:31:12.366463+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=60689.8
- Funnel: target 1097 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +59.40% | $2,417,046.86 |
| SI/USDT:USDT | +54.29% | $1,437,931.23 |
| KOR/USDT:USDT | +33.86% | $1,808,835.57 |
| SOXL/USDT:USDT | +28.68% | $1,752,303,359.63 |
| SSV/USDT:USDT | +22.51% | $1,829,416.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVE/USDT:USDT | below_1h_threshold | +2.78% | +2.47% |
| BULLA/USDT:USDT | below_1h_threshold | +2.58% | +2.26% |
| NVDL/USDT:USDT | below_1h_threshold | +1.47% | +1.16% |
| SOXL/USDT:USDT | below_1h_threshold | +1.04% | +0.72% |
| SEI/USDT:USDT | below_1h_threshold | +0.97% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
