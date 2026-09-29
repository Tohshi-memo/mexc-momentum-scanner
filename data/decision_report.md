# Decision Report

- generated_at: 2026-09-29T10:56:30.080114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15760**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=15760, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/17 | 35.3% | +2.81% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.41% | **+0.31%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.23% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.88% | **+2.88%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.91% | **+0.50%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.35% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5985件 (Win 1766 / Loss 1925 / Flat 2294) / skip 6336件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5637件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3922件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T10:56:15.559065+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=84033.8
- Funnel: target 1067 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +37.27% | $17,653,253.51 |
| GRASS/USDT:USDT | +26.19% | $8,260,886.24 |
| 0G/USDT:USDT | +22.24% | $1,911,543.51 |
| CRV/USDT:USDT | +20.15% | $18,691,802.20 |
| NMR/USDT:USDT | +19.44% | $13,149,255.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NMR/USDT:USDT | below_1h_threshold | +2.65% | +2.86% |
| AAVE/USDT:USDT | below_1h_threshold | +1.70% | +1.92% |
| SKY/USDT:USDT | below_1h_threshold | +1.65% | +1.86% |
| 0G/USDT:USDT | below_1h_threshold | +1.62% | +1.83% |
| GALA/USDT:USDT | below_1h_threshold | +1.57% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
