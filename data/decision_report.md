# Decision Report

- generated_at: 2026-07-23T15:46:18.947242+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9374**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=9374, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_BB3S | 7/19 | 36.8% | +3.02% | **+1.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.22% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.26% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.17%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3321件 (Win 1048 / Loss 1075 / Flat 1198) / skip 2614件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1623件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0185 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.06** / 初期 $100.00 (+1.06%)
- 確定: 440件 (Win 145 / Loss 180 / Flat 115) / pending 4件 / skip 401件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000097 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $101.06

## 6. Latest Market Context

- 更新: 2026-07-23T15:46:10.903403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64873.2
- Funnel: target 897 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +86.02% | $10,469,004.69 |
| BANK/USDT:USDT | +36.83% | $109,940,957.08 |
| JIMOTHY/USDT:USDT | +29.22% | $5,745,967.84 |
| ZAMA/USDT:USDT | +28.71% | $7,487,859.58 |
| ON/USDT:USDT | +15.40% | $5,932,449.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.07% | +4.08% |
| EVAA/USDT:USDT | below_1h_threshold | +2.46% | +2.47% |
| MUU/USDT:USDT | below_1h_threshold | +2.44% | +2.46% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.94% |
| BEAT/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
