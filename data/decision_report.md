# Decision Report

- generated_at: 2026-08-10T06:11:26.350815+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11130**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=11130, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.67% | **+1.34%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.93% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.08% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.75% | **+6.75%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.09% | **+0.93%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.69% | **+0.59%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3758件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3028件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.50** / 初期 $100.00 (+17.50%)
- 確定: 1285件 (Win 398 / Loss 494 / Flat 393) / pending 1件 / skip 1315件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.50

## 6. Latest Market Context

- 更新: 2026-08-10T06:11:18.778299+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=65153.4
- Funnel: target 963 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +65.39% | $20,708,629.62 |
| CAP/USDT:USDT | +32.01% | $3,510,840.92 |
| TUT/USDT:USDT | +23.21% | $80,570,919.83 |
| CASHCAT/USDT:USDT | +21.48% | $1,290,378.28 |
| GRVT/USDT:USDT | +18.34% | $1,325,861.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +3.65% | +3.60% |
| NIL/USDT:USDT | below_1h_threshold | +2.74% | +2.68% |
| TUT/USDT:USDT | below_1h_threshold | +2.55% | +2.49% |
| PEOPLE/USDT:USDT | below_1h_threshold | +2.46% | +2.40% |
| CAP/USDT:USDT | below_1h_threshold | +2.09% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
