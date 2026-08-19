# Decision Report

- generated_at: 2026-08-19T13:51:40.075534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11979**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=11979, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.75% | **+0.43%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.28% | **+0.20%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.19% | **+0.10%** |
| LIMIT_4PCT | 8/20 | 40.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.38% | **-0.17%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.51% | **-0.46%** |
| MARKET_LONG | 20/20 | 100.0% | -0.50% | **-0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$608.52** / 初期 $100.00 (+508.52%)
- 確定: 4240件 (Win 1302 / Loss 1387 / Flat 1551) / skip 4300件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $608.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3569件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.38** / 初期 $100.00 (+17.38%)
- 確定: 1751件 (Win 520 / Loss 667 / Flat 564) / pending 2件 / skip 1699件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.38

## 6. Latest Market Context

- 更新: 2026-08-19T13:51:22.490798+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=65086.8
- Funnel: target 997 → liquid 185 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +73.30% | $106,769,173.59 |
| HEMI/USDT:USDT | +44.63% | $5,123,330.05 |
| STAR/USDT:USDT | +27.37% | $1,109,356.90 |
| UNITREE/USDT:USDT | +19.02% | $17,672,566.21 |
| MVLL/USDT:USDT | +17.14% | $5,214,266.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.77% | +2.41% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.35% | +1.99% |
| CYS/USDT:USDT | below_1h_threshold | +2.29% | +1.94% |
| ZRO/USDT:USDT | below_1h_threshold | +2.27% | +1.92% |
| STAR/USDT:USDT | below_1h_threshold | +1.99% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
