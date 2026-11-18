# Decision Report

- generated_at: 2026-11-18T11:56:45.161059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19145**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=19145, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.96% | **+2.52%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.51% | **+2.39%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.32% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.84% | **+0.38%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.46% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7353件 (Win 2109 / Loss 2358 / Flat 2886) / skip 8353件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$432.53** / 初期 $100.00 (+332.53%)
- 確定: 5000件 (Win 1334 / Loss 1084 / Flat 2582) / skip 7556件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $432.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7308件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000152 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T11:56:25.080100+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=64249.7
- Funnel: target 1080 → liquid 146 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +109.31% | $7,233,518.68 |
| PIPPIN/USDT:USDT | +83.40% | $3,021,670.87 |
| ICNT/USDT:USDT | +36.09% | $4,978,613.82 |
| IRYS/USDT:USDT | +25.48% | $2,551,328.46 |
| CLAUDIA/USDT:USDT | +22.35% | $1,104,612.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +4.41% | +4.56% |
| USELESS/USDT:USDT | below_1h_threshold | +2.01% | +2.15% |
| PONS/USDT:USDT | below_1h_threshold | +1.02% | +1.16% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.95% | +1.09% |
| KAVA/USDT:USDT | below_1h_threshold | +0.68% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
