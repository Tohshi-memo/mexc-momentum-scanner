# Decision Report

- generated_at: 2026-10-23T04:06:15.879883+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17187**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=17187, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.44% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.80% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.30% | **+1.27%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.15% | **+0.10%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.01% | **+0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,330.78** / 初期 $100.00 (+1230.78%)
- 確定: 6543件 (Win 1900 / Loss 2087 / Flat 2556) / skip 7205件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,330.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.12** / 初期 $100.00 (+177.12%)
- 確定: 3863件 (Win 1057 / Loss 900 / Flat 1906) / skip 6735件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $277.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5348件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T04:06:05.965537+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81823.9
- Funnel: target 1096 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +37.41% | $12,759,497.57 |
| AGT/USDT:USDT | +29.51% | $5,607,839.32 |
| IRYS/USDT:USDT | +15.86% | $3,708,468.74 |
| DNA/USDT:USDT | +14.50% | $4,226,730.68 |
| DASH/USDT:USDT | +10.28% | $20,348,484.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.17% | +2.22% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.12% | +2.16% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.85% | +1.89% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.83% | +1.88% |
| BTW/USDT:USDT | below_1h_threshold | +1.14% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
