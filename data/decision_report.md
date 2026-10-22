# Decision Report

- generated_at: 2026-10-22T07:36:22.541141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17124**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=17124, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.34% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.58% | **+0.95%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.17% | **+0.82%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.37** / 初期 $100.00 (+1242.37%)
- 確定: 6506件 (Win 1892 / Loss 2076 / Flat 2538) / skip 7179件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.18% 残高後 $1,342.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.59** / 初期 $100.00 (+178.59%)
- 確定: 3834件 (Win 1054 / Loss 898 / Flat 1882) / skip 6701件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.14% 残高後 $278.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5285件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000097 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T07:36:10.510489+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=82247.9
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +38.05% | $2,332,426.69 |
| PTB/USDT:USDT | +28.33% | $1,270,882.47 |
| BTW/USDT:USDT | +22.03% | $32,449,462.63 |
| AGT/USDT:USDT | +12.20% | $5,312,636.66 |
| SOXS/USDT:USDT | +10.79% | $11,286,359.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +1.92% | +2.17% |
| BTW/USDT:USDT | below_1h_threshold | +1.86% | +2.11% |
| IRYS/USDT:USDT | below_1h_threshold | +1.81% | +2.07% |
| BAT/USDT:USDT | below_1h_threshold | +1.75% | +2.01% |
| JCT/USDT:USDT | below_1h_threshold | +1.62% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
