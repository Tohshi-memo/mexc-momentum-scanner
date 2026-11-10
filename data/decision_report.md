# Decision Report

- generated_at: 2026-11-10T13:36:31.196314+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18598**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=18598, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.02% | **+0.30%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.32% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,662.00** / 初期 $100.00 (+1562.00%)
- 確定: 7195件 (Win 2069 / Loss 2298 / Flat 2828) / skip 7964件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.14% 残高後 $1,662.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$394.54** / 初期 $100.00 (+294.54%)
- 確定: 4764件 (Win 1281 / Loss 1050 / Flat 2433) / skip 7245件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0523 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $394.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6756件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000254 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T13:36:17.563694+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.73% price=73814.1
- Funnel: target 1099 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +68.06% | $19,158,981.94 |
| ONE/USDT:USDT | +22.20% | $9,484,952.18 |
| ARIA/USDT:USDT | +11.20% | $2,630,052.15 |
| BR/USDT:USDT | +10.70% | $3,648,343.50 |
| ZHIPUSTOCK/USDT:USDT | +9.04% | $1,601,125.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +2.96% | +3.69% |
| AIOT/USDT:USDT | below_1h_threshold | +2.52% | +3.25% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.51% | +2.25% |
| BR/USDT:USDT | below_1h_threshold | +1.42% | +2.15% |
| SOXS/USDT:USDT | below_1h_threshold | +0.76% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
