# Decision Report

- generated_at: 2026-11-13T05:56:32.208728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18785**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=18785, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.41%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.54% | **+1.31%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.06% | **+1.34%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.72%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,724.02** / 初期 $100.00 (+1624.02%)
- 確定: 7255件 (Win 2089 / Loss 2324 / Flat 2842) / skip 8091件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KGEN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,724.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$401.55** / 初期 $100.00 (+301.55%)
- 確定: 4804件 (Win 1294 / Loss 1065 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KGEN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $401.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6945件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T05:56:11.519769+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=68472.1
- Funnel: target 1105 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +50.17% | $10,409,513.64 |
| KOR/USDT:USDT | +40.90% | $1,697,061.59 |
| ARIA/USDT:USDT | +37.03% | $9,450,942.20 |
| CBRSSTOCK/USDT:USDT | +11.36% | $3,531,850.27 |
| GANG/USDT:USDT | +10.85% | $1,172,698.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVD/USDT:USDT | below_1h_threshold | +4.58% | +4.70% |
| MAGMA/USDT:USDT | below_1h_threshold | +4.39% | +4.51% |
| PONS/USDT:USDT | below_1h_threshold | +2.61% | +2.73% |
| USELESS/USDT:USDT | below_1h_threshold | +1.61% | +1.73% |
| H/USDT:USDT | below_1h_threshold | +1.60% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
