# Decision Report

- generated_at: 2026-11-18T04:51:25.252504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19113**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19113, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.58% | **+0.29%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.38% | **+0.10%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.63% | **+1.31%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.27% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.86% | **+0.64%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8322件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$431.95** / 初期 $100.00 (+331.95%)
- 確定: 4997件 (Win 1333 / Loss 1084 / Flat 2580) / skip 7527件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $431.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7275件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000134 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T04:51:15.457346+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64440.3
- Funnel: target 1073 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +25.70% | $2,376,258.64 |
| ICNT/USDT:USDT | +24.07% | $1,826,056.07 |
| CSOPSKHYNIX2L/USDT:USDT | +13.34% | $1,028,965.30 |
| MUU/USDT:USDT | +12.56% | $34,272,957.44 |
| MVLL/USDT:USDT | +12.18% | $5,394,712.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +3.29% | +3.27% |
| ICNT/USDT:USDT | below_1h_threshold | +3.18% | +3.15% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |
| KORU/USDT:USDT | below_1h_threshold | +2.11% | +2.09% |
| BREV/USDT:USDT | below_1h_threshold | +1.87% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
