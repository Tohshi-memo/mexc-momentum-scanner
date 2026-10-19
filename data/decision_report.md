# Decision Report

- generated_at: 2026-10-19T08:21:20.680886+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=17005, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.04% | **+0.93%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.85% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.37% | **+0.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.24% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.29% | **+0.65%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +1.21% | **+0.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,257.35** / 初期 $100.00 (+1157.35%)
- 確定: 6450件 (Win 1871 / Loss 2061 / Flat 2518) / skip 7116件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $1,257.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3770件 (Win 1038 / Loss 883 / Flat 1849) / skip 6646件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0032 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5164件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T08:21:06.121670+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=82815.5
- Funnel: target 1085 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +42.75% | $8,901,710.52 |
| ZEREBRO/USDT:USDT | +25.10% | $1,811,251.83 |
| KORU/USDT:USDT | +20.56% | $67,996,775.73 |
| UNITREE/USDT:USDT | +17.21% | $1,790,516.82 |
| CT/USDT:USDT | +13.78% | $1,987,423.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +1.49% | +1.34% |
| RIVER/USDT:USDT | below_1h_threshold | +1.25% | +1.11% |
| INJ/USDT:USDT | below_1h_threshold | +0.96% | +0.81% |
| ARB/USDT:USDT | below_1h_threshold | +0.92% | +0.78% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
