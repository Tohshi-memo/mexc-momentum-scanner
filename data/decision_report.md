# Decision Report

- generated_at: 2026-10-19T15:06:31.263085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17013**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.32% / filled 20/20。**
- 全期間 MARKET基準: n=17013, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.15% | **+1.83%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.71% | **+0.35%** |
| LIMIT_BB3S | 7/16 | 43.8% | +0.38% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.35% | **-0.19%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.49% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,257.25** / 初期 $100.00 (+1157.25%)
- 確定: 6458件 (Win 1872 / Loss 2063 / Flat 2523) / skip 7116件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,257.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3778件 (Win 1038 / Loss 883 / Flat 1857) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0302 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5173件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T15:06:19.091497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=82270.0
- Funnel: target 1090 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +26.91% | $10,792,982.65 |
| BR/USDT:USDT | +25.29% | $21,024,700.79 |
| SNXX/USDT:USDT | +21.32% | $41,017,736.48 |
| KORU/USDT:USDT | +20.47% | $121,691,428.89 |
| AVA/USDT:USDT | +17.52% | $1,765,017.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.62% | +3.62% |
| ZRO/USDT:USDT | below_1h_threshold | +3.01% | +3.01% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +2.15% | +2.15% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.99% | +1.99% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.90% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
