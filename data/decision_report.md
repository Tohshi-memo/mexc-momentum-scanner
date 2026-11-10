# Decision Report

- generated_at: 2026-11-10T17:46:25.561288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.26% / filled 20/20。**
- 全期間 MARKET基準: n=18622, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+4.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.26% | **+4.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.26% | **+4.26%** |
| LIMIT_1PCT | 10/20 | 50.0% | +2.93% | **+1.47%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.67% | **+0.59%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.58% | **+0.55%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.48% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_FIB1618_LONG | 12/20 | 60.0% | -1.10% | **-0.66%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -1.05% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7209件 (Win 2073 / Loss 2305 / Flat 2831) / skip 7974件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7256件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0358 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6788件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000510 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T17:46:11.088726+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=72869.0
- Funnel: target 1099 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +9.79% | $35,580,639.83 |
| SOXS/USDT:USDT | +3.10% | $37,962,985.82 |
| AIN/USDT:USDT | +2.64% | $1,649,665.71 |
| BTW/USDT:USDT | +2.30% | $4,151,498.95 |
| SQQQ/USDT:USDT | +2.15% | $3,009,781.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +4.23% | +4.20% |
| BTW/USDT:USDT | below_1h_threshold | +3.50% | +3.47% |
| SOXS/USDT:USDT | below_1h_threshold | +3.00% | +2.97% |
| NGAS/USDT:USDT | below_1h_threshold | +2.00% | +1.96% |
| PEPE/USDT:USDT | below_1h_threshold | +1.33% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
