# Decision Report

- generated_at: 2026-11-26T17:46:25.315947+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19714, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.81% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.38% | **+1.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.65% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.16** / 初期 $100.00 (+1848.16%)
- 確定: 7639件 (Win 2199 / Loss 2459 / Flat 2981) / skip 8636件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,948.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.54** / 初期 $100.00 (+367.54%)
- 確定: 5240件 (Win 1396 / Loss 1127 / Flat 2717) / skip 7885件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0079 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $467.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T17:46:08.973892+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=60419.8
- Funnel: target 1097 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +9.39% | $1,271,409.85 |
| SI/USDT:USDT | +5.94% | $1,998,750.54 |
| SSV/USDT:USDT | +3.74% | $2,865,477.02 |
| MANTRA/USDT:USDT | +3.66% | $4,366,494.61 |
| AIOT/USDT:USDT | +3.55% | $1,125,547.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANTRA/USDT:USDT | below_1h_threshold | +3.23% | +3.36% |
| AIOT/USDT:USDT | below_1h_threshold | +2.63% | +2.76% |
| SSV/USDT:USDT | below_1h_threshold | +2.34% | +2.48% |
| SI/USDT:USDT | below_1h_threshold | +1.31% | +1.44% |
| SOXS/USDT:USDT | below_1h_threshold | +1.19% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
