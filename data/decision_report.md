# Decision Report

- generated_at: 2026-09-30T10:06:18.988090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15827**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15827, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.25% | **-0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_BB3S | 7/18 | 38.9% | -0.12% | **-0.05%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.31% | **-0.08%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.32% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.87% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.77% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,221.11** / 初期 $100.00 (+1121.11%)
- 確定: 5988件 (Win 1766 / Loss 1926 / Flat 2296) / skip 6400件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,221.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3536件 (Win 974 / Loss 812 / Flat 1750) / skip 5702件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3987件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-30T10:06:07.622844+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=83724.0
- Funnel: target 1079 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +105.47% | $7,817,945.30 |
| MOVR/USDT:USDT | +71.09% | $2,448,766.68 |
| PHA/USDT:USDT | +17.42% | $5,306,922.72 |
| SOONNETWORK/USDT:USDT | +16.35% | $5,383,367.37 |
| ARK/USDT:USDT | +16.20% | $1,225,092.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +3.93% | +3.78% |
| NIL/USDT:USDT | below_1h_threshold | +3.07% | +2.91% |
| GRASS/USDT:USDT | below_1h_threshold | +2.32% | +2.16% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.87% | +1.71% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.02% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
