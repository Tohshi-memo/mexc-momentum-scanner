# Decision Report

- generated_at: 2026-08-19T13:46:41.011252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11977**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=11977, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.75% | **+0.46%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.19% | **+0.16%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.65** / 初期 $100.00 (+514.65%)
- 確定: 4238件 (Win 1302 / Loss 1385 / Flat 1551) / skip 4300件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $614.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3567件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.38** / 初期 $100.00 (+17.38%)
- 確定: 1751件 (Win 520 / Loss 667 / Flat 564) / pending 2件 / skip 1698件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.38

## 6. Latest Market Context

- 更新: 2026-08-19T13:46:25.739488+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=64996.2
- Funnel: target 997 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +66.40% | $105,931,201.46 |
| HEMI/USDT:USDT | +43.41% | $5,069,650.37 |
| STAR/USDT:USDT | +26.97% | $1,103,178.80 |
| MVLL/USDT:USDT | +21.17% | $5,186,112.97 |
| UNITREE/USDT:USDT | +18.57% | $17,658,102.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKUU/USDT:USDT | below_1h_threshold | +3.84% | +3.63% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.77% | +2.55% |
| ZRO/USDT:USDT | below_1h_threshold | +2.56% | +2.34% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.35% | +2.13% |
| BTW/USDT:USDT | below_1h_threshold | +2.32% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
