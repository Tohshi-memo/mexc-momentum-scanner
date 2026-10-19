# Decision Report

- generated_at: 2026-10-19T08:16:17.069664+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17004**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=17004, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.85% | **+0.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.42% | **+0.38%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.47% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +1.21% | **+0.42%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.24% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,257.35** / 初期 $100.00 (+1157.35%)
- 確定: 6449件 (Win 1871 / Loss 2061 / Flat 2517) / skip 7116件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,257.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3769件 (Win 1038 / Loss 883 / Flat 1848) / skip 6646件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5163件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T08:16:07.312759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=82669.6
- Funnel: target 1085 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +38.88% | $8,724,075.08 |
| ZEREBRO/USDT:USDT | +25.07% | $1,805,033.45 |
| KORU/USDT:USDT | +19.98% | $67,933,016.53 |
| CT/USDT:USDT | +17.10% | $1,952,495.87 |
| UNITREE/USDT:USDT | +17.01% | $1,765,650.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +1.73% | +1.76% |
| CT/USDT:USDT | below_1h_threshold | +0.87% | +0.90% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.78% |
| RIVER/USDT:USDT | below_1h_threshold | +0.68% | +0.71% |
| UNITREE/USDT:USDT | below_1h_threshold | +0.55% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
