# Decision Report

- generated_at: 2026-11-18T02:11:24.149545+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19111**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19111, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.55% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.83% | **+0.82%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.72% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8320件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$431.95** / 初期 $100.00 (+331.95%)
- 確定: 4997件 (Win 1333 / Loss 1084 / Flat 2580) / skip 7525件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $431.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7273件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000134 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T02:11:10.685948+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=64443.9
- Funnel: target 1073 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +18.05% | $2,128,865.97 |
| ICNT/USDT:USDT | +17.03% | $1,254,610.90 |
| MUU/USDT:USDT | +12.71% | $35,361,183.13 |
| SNXX/USDT:USDT | +11.85% | $48,050,899.25 |
| CSOPSKHYNIX2L/USDT:USDT | +11.68% | $1,227,459.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UVXY/USDT:USDT | below_1h_threshold | +3.81% | +3.54% |
| AXIS/USDT:USDT | below_1h_threshold | +2.97% | +2.70% |
| BLESS/USDT:USDT | below_1h_threshold | +2.66% | +2.40% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.52% | +2.25% |
| GRAM/USDT:USDT | below_1h_threshold | +1.11% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
