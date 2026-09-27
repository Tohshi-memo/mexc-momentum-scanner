# Decision Report

- generated_at: 2026-09-27T15:56:29.177904+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15650**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.88% / filled 20/20。**
- 全期間 MARKET基準: n=15650, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.22% | **+1.78%** |
| LIMIT_BB3S | 5/16 | 31.2% | +3.21% | **+1.00%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.01%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.65% | **-0.10%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.91% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5980件 (Win 1766 / Loss 1923 / Flat 2291) / skip 6231件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5527件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.97** / 初期 $100.00 (+18.97%)
- 確定: 3232件 (Win 946 / Loss 1276 / Flat 1010) / pending 4件 / skip 3885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000087 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SUI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $118.97

## 6. Latest Market Context

- 更新: 2026-09-27T15:56:15.342768+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=84429.8
- Funnel: target 1069 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1, 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOONNETWORK/USDT:USDT | +55.46% | $3,515,998.12 |
| QNT/USDT:USDT | +52.51% | $156,783,811.50 |
| ARX/USDT:USDT | +28.88% | $1,088,089.79 |
| W/USDT:USDT | +19.04% | $3,312,276.88 |
| GRASS/USDT:USDT | +16.27% | $7,330,623.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| W/USDT:USDT | below_1h_threshold | +4.19% | +4.26% |
| GRAM/USDT:USDT | below_1h_threshold | +4.04% | +4.10% |
| ENA/USDT:USDT | below_1h_threshold | +1.96% | +2.03% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.57% | +1.64% |
| FLOW/USDT:USDT | below_1h_threshold | +1.38% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
