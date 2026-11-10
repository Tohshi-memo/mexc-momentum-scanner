# Decision Report

- generated_at: 2026-11-10T22:16:28.760784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18628**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +5.49% / filled 20/20。**
- 全期間 MARKET基準: n=18628, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+5.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +5.49% | **+5.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +5.49% | **+5.49%** |
| LIMIT_1PCT | 10/20 | 50.0% | +5.50% | **+2.75%** |
| LIMIT_2PCT | 5/20 | 25.0% | +4.13% | **+1.03%** |
| LIMIT_3PCT | 4/20 | 20.0% | +3.66% | **+0.73%** |
| LIMIT_ATR | 6/20 | 30.0% | +1.99% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.05% | **-0.03%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_FIB1618_LONG | 12/20 | 60.0% | -1.10% | **-0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7209件 (Win 2073 / Loss 2305 / Flat 2831) / skip 7980件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7262件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0224 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6791件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000578 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T22:16:15.415328+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=73883.9
- Funnel: target 1099 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +6.65% | $2,993,196.78 |
| INJ/USDT:USDT | +5.21% | $16,550,879.35 |
| MUU/USDT:USDT | +4.90% | $14,475,423.22 |
| LIT/USDT:USDT | +4.83% | $9,968,085.75 |
| GRAM/USDT:USDT | +4.82% | $2,400,172.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.27% | +3.19% |
| ONE/USDT:USDT | below_1h_threshold | +2.95% | +2.87% |
| ICP/USDT:USDT | below_1h_threshold | +1.23% | +1.14% |
| SOXL/USDT:USDT | below_1h_threshold | +1.22% | +1.13% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.10% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
