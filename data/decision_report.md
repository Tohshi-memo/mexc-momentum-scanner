# Decision Report

- generated_at: 2026-10-19T02:46:24.495135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16972**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=16972, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.79% | **+1.16%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.35% | **+1.01%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.62% | **+0.89%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.89% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 245件 (TP 91 / SL 147 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,274.92** / 初期 $100.00 (+1174.92%)
- 確定: 6417件 (Win 1867 / Loss 2052 / Flat 2498) / skip 7116件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $1,274.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.84** / 初期 $100.00 (+176.84%)
- 確定: 3737件 (Win 1034 / Loss 881 / Flat 1822) / skip 6646件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0854 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEREBRO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $276.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5130件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000329 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T02:46:10.197508+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=82534.8
- Funnel: target 1084 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +20.74% | $1,243,260.75 |
| APR/USDT:USDT | +15.78% | $1,966,172.37 |
| KORU/USDT:USDT | +15.67% | $38,672,976.09 |
| UNITREE/USDT:USDT | +13.02% | $1,001,186.40 |
| VVV/USDT:USDT | +12.79% | $3,347,052.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +4.07% | +3.93% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.07% | +3.92% |
| UNITREE/USDT:USDT | below_1h_threshold | +3.83% | +3.68% |
| VVV/USDT:USDT | below_1h_threshold | +3.13% | +2.98% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.81% | +2.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
