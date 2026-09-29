# Decision Report

- generated_at: 2026-09-29T19:37:58.691665+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15790**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=15790, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.82% | **+0.99%** |
| LIMIT_BB3S | 9/17 | 52.9% | +1.41% | **+0.75%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.65% | **+0.74%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.23% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.13% | **+1.81%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.39% | **+1.79%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.37% | **+1.58%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.33% | **+1.26%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5986件 (Win 1766 / Loss 1925 / Flat 2295) / skip 6365件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5666件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0423 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3955件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T19:37:44.463219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=83525.2
- Funnel: target 1073 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1, 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +51.28% | $1,669,052.04 |
| QNT/USDT:USDT | +8.41% | $332,198,172.73 |
| GRASS/USDT:USDT | +7.58% | $9,941,780.54 |
| SOONNETWORK/USDT:USDT | +5.34% | $2,832,129.01 |
| NIL/USDT:USDT | +5.19% | $2,678,861.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +2.72% | +2.82% |
| KORU/USDT:USDT | below_1h_threshold | +2.44% | +2.54% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.09% | +2.19% |
| BTW/USDT:USDT | below_1h_threshold | +2.01% | +2.12% |
| FET/USDT:USDT | below_1h_threshold | +1.79% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
