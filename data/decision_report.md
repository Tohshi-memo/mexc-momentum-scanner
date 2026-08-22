# Decision Report

- generated_at: 2026-08-22T07:36:18.958765+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12354**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.75% / filled 20/20。**
- 全期間 MARKET基準: n=12354, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.75% | **+3.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.75% | **+3.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.89% | **+2.31%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.45% | **+1.47%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.42% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.11% | **-0.07%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | -0.74% | **-0.33%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.63% | **-0.41%** |
| LIMIT_10PCT_LONG | 8/20 | 40.0% | -1.69% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.07** / 初期 $100.00 (+616.07%)
- 確定: 4447件 (Win 1364 / Loss 1453 / Flat 1630) / skip 4468件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3831件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.04** / 初期 $100.00 (+17.04%)
- 確定: 1862件 (Win 549 / Loss 705 / Flat 608) / pending 0件 / skip 1968件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000630 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.04

## 6. Latest Market Context

- 更新: 2026-08-22T07:36:09.307803+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77419.6
- Funnel: target 1018 → liquid 250 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 92.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +230.30% | $5,535,715.56 |
| TRUMPOFFICIAL/USDT:USDT | +53.28% | $107,612,162.47 |
| CATE/USDT:USDT | +47.88% | $11,528,578.98 |
| AGI/USDT:USDT | +34.55% | $2,094,936.23 |
| ZAMA/USDT:USDT | +32.41% | $1,764,086.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.35% | +4.42% |
| ZEN/USDT:USDT | below_1h_threshold | +3.74% | +3.82% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.67% | +3.75% |
| PEPE/USDT:USDT | below_1h_threshold | +3.23% | +3.30% |
| AR/USDT:USDT | below_1h_threshold | +2.41% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
