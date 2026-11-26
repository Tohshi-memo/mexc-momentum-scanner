# Decision Report

- generated_at: 2026-11-26T10:26:36.211654+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19684**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.09% / filled 20/20。**
- 全期間 MARKET基準: n=19684, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.35% | **+1.88%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.18% | **+1.09%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.29% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.05% | **+0.01%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.56% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.11** / 初期 $100.00 (+1888.11%)
- 確定: 7620件 (Win 2195 / Loss 2454 / Flat 2971) / skip 8625件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,988.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7874件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7847件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T10:26:19.402676+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=60817.8
- Funnel: target 1097 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +70.57% | $3,127,363.73 |
| SI/USDT:USDT | +54.19% | $1,467,587.75 |
| KOR/USDT:USDT | +40.64% | $1,930,806.50 |
| SOXL/USDT:USDT | +28.91% | $1,639,035,629.47 |
| INIT/USDT:USDT | +27.02% | $1,555,978.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ELSA/USDT:USDT | below_1h_threshold | +2.48% | +2.63% |
| SI/USDT:USDT | below_1h_threshold | +2.19% | +2.34% |
| BULLA/USDT:USDT | below_1h_threshold | +1.61% | +1.76% |
| ZRO/USDT:USDT | below_1h_threshold | +1.09% | +1.24% |
| SEI/USDT:USDT | below_1h_threshold | +0.84% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
