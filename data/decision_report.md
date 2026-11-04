# Decision Report

- generated_at: 2026-11-04T10:06:14.248817+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18114**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=18114, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.68% | **+1.43%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_BB3S | 8/19 | 42.1% | +2.13% | **+0.90%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.88% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -1.10% | **-0.50%** |
| MARKET_LONG | 20/20 | 100.0% | -0.54% | **-0.54%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,498.69** / 初期 $100.00 (+1398.69%)
- 確定: 6933件 (Win 2004 / Loss 2223 / Flat 2706) / skip 7742件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXIS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,498.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.27** / 初期 $100.00 (+273.27%)
- 確定: 4528件 (Win 1212 / Loss 1014 / Flat 2302) / skip 6997件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXIS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $373.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6274件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000122 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T10:06:05.488937+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78389.2
- Funnel: target 1073 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +24.07% | $3,778,578.95 |
| BMT/USDT:USDT | +16.34% | $1,644,724.14 |
| IDOL/USDT:USDT | +11.37% | $8,830,726.22 |
| LSK/USDT:USDT | +10.94% | $3,344,017.01 |
| FLUID/USDT:USDT | +10.52% | $1,293,536.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.06% | +1.04% |
| GRASS/USDT:USDT | below_1h_threshold | +0.78% | +0.77% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| INJ/USDT:USDT | below_1h_threshold | +0.56% | +0.55% |
| STX/USDT:USDT | below_1h_threshold | +0.53% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
