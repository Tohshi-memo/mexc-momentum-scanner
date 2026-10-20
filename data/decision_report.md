# Decision Report

- generated_at: 2026-10-20T08:11:19.493382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17047**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.09% / filled 20/20。**
- 全期間 MARKET基準: n=17047, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.94% | **+1.74%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.20% | **+0.03%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.13** / 初期 $100.00 (+1198.13%)
- 確定: 6476件 (Win 1882 / Loss 2066 / Flat 2528) / skip 7132件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.69% 残高後 $1,298.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3801件 (Win 1044 / Loss 886 / Flat 1871) / skip 6657件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0346 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5207件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T08:11:07.271107+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=81356.4
- Funnel: target 1084 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +43.68% | $1,779,072.39 |
| ALT/USDT:USDT | +24.19% | $1,340,156.50 |
| PHA/USDT:USDT | +19.29% | $18,047,325.14 |
| BR/USDT:USDT | +13.68% | $43,966,278.69 |
| A/USDT:USDT | +11.66% | $23,167,147.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.61% | +1.81% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.98% | +1.18% |
| USOIL/USDT:USDT | below_1h_threshold | +0.96% | +1.16% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.79% | +0.99% |
| JCT/USDT:USDT | below_1h_threshold | +0.75% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
