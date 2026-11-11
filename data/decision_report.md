# Decision Report

- generated_at: 2026-11-11T03:11:23.763239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18637**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.98% / filled 20/20。**
- 全期間 MARKET基準: n=18637, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.98% | **+2.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.98% | **+2.98%** |
| LIMIT_1PCT | 12/20 | 60.0% | +2.86% | **+1.72%** |
| LIMIT_3PCT | 7/20 | 35.0% | +2.96% | **+1.04%** |
| LIMIT_2PCT | 8/20 | 40.0% | +2.17% | **+0.87%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.08% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.21% | **-0.07%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7210件 (Win 2073 / Loss 2305 / Flat 2832) / skip 7988件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7271件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6796件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000662 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T03:11:10.422070+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=73830.6
- Funnel: target 1099 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FLOAT/USDT:USDT | +31.68% | $1,041,584.49 |
| CRWVSTOCK/USDT:USDT | +16.20% | $5,961,574.24 |
| JCT/USDT:USDT | +12.73% | $17,305,381.57 |
| MUU/USDT:USDT | +12.71% | $14,571,361.44 |
| SOXL/USDT:USDT | +12.56% | $660,896,449.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +3.20% | +2.91% |
| KORU/USDT:USDT | below_1h_threshold | +2.05% | +1.76% |
| PYTH/USDT:USDT | below_1h_threshold | +1.32% | +1.02% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.02% |
| USELESS/USDT:USDT | below_1h_threshold | +1.27% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
