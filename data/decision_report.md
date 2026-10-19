# Decision Report

- generated_at: 2026-10-19T09:46:20.604634+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17008**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=17008, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.16% | **+1.73%** |
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.75% | **+1.58%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.03% | **+0.62%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.96% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.82%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.81% | **+0.45%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +0.91% | **+0.36%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,263.57** / 初期 $100.00 (+1163.57%)
- 確定: 6453件 (Win 1872 / Loss 2062 / Flat 2519) / skip 7116件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KIOXIASTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,263.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3773件 (Win 1038 / Loss 883 / Flat 1852) / skip 6646件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5168件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000093 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T09:46:09.085608+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=82980.5
- Funnel: target 1085 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +22.63% | $10,469,266.68 |
| ZEREBRO/USDT:USDT | +21.60% | $1,879,934.82 |
| KORU/USDT:USDT | +20.66% | $69,939,158.29 |
| CT/USDT:USDT | +16.97% | $3,268,734.94 |
| UNITREE/USDT:USDT | +16.56% | $1,872,475.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.11% | +3.87% |
| Q/USDT:USDT | below_1h_threshold | +2.53% | +2.30% |
| STX/USDT:USDT | below_1h_threshold | +2.41% | +2.18% |
| QNT/USDT:USDT | below_1h_threshold | +1.96% | +1.72% |
| UAI/USDT:USDT | below_1h_threshold | +1.55% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
