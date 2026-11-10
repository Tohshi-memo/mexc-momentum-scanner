# Decision Report

- generated_at: 2026-11-10T18:26:20.016305+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.86% / filled 20/20。**
- 全期間 MARKET基準: n=18625, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+4.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.86% | **+4.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.86% | **+4.86%** |
| LIMIT_1PCT | 9/20 | 45.0% | +5.04% | **+2.27%** |
| LIMIT_2PCT | 5/20 | 25.0% | +3.61% | **+0.90%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_6PCT_LONG | 15/20 | 75.0% | -0.52% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7209件 (Win 2073 / Loss 2305 / Flat 2831) / skip 7977件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7259件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0173 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6789件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000455 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T18:26:09.424951+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73226.6
- Funnel: target 1099 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +12.53% | $38,442,800.67 |
| BTW/USDT:USDT | +4.95% | $4,837,271.43 |
| AIN/USDT:USDT | +4.94% | $1,652,069.57 |
| NGAS/USDT:USDT | +2.43% | $2,761,502.03 |
| XRP/USDT:USDT | +1.82% | $311,529,038.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +3.18% | +3.22% |
| CAP/USDT:USDT | below_1h_threshold | +1.82% | +1.86% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| Q/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| AIN/USDT:USDT | below_1h_threshold | +1.27% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
