# Decision Report

- generated_at: 2026-11-10T14:16:11.971273+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18600**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=18600, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.82% | **+0.64%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.58% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.10% | **+0.49%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.75% | **+0.48%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.02% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,664.13** / 初期 $100.00 (+1564.13%)
- 確定: 7197件 (Win 2070 / Loss 2299 / Flat 2828) / skip 7964件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,664.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$393.16** / 初期 $100.00 (+293.16%)
- 確定: 4766件 (Win 1281 / Loss 1051 / Flat 2434) / skip 7245件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0434 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $393.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6757件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T14:16:02.516355+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=73880.1
- Funnel: target 1099 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +63.60% | $21,074,249.21 |
| ONE/USDT:USDT | +20.29% | $9,414,765.50 |
| ARIA/USDT:USDT | +13.18% | $2,647,800.46 |
| BR/USDT:USDT | +11.30% | $3,663,756.04 |
| ZHIPUSTOCK/USDT:USDT | +9.59% | $1,606,210.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +4.73% | +4.50% |
| SQQQ/USDT:USDT | below_1h_threshold | +2.89% | +2.67% |
| LIT/USDT:USDT | below_1h_threshold | +1.31% | +1.08% |
| AIN/USDT:USDT | below_1h_threshold | +1.24% | +1.01% |
| ARIA/USDT:USDT | below_1h_threshold | +0.85% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
