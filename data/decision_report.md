# Decision Report

- generated_at: 2026-11-26T13:31:48.455472+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19695**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=19695, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.75% | **+0.49%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.02%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.78% | **+0.54%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,995.22** / 初期 $100.00 (+1895.22%)
- 確定: 7629件 (Win 2198 / Loss 2454 / Flat 2977) / skip 8627件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,995.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.98** / 初期 $100.00 (+365.98%)
- 確定: 5222件 (Win 1390 / Loss 1125 / Flat 2707) / skip 7884件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $465.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7857件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T13:31:33.579086+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60825.4
- Funnel: target 1097 → liquid 150 → pre 50 → checked 49 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 91.5 >= 65=1, 4h RSI 83.6 >= 65=1, 4h RSI 65.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +95.06% | $6,046,625.55 |
| SI/USDT:USDT | +69.92% | $1,722,760.56 |
| NES/USDT:USDT | +54.07% | $1,078,818.01 |
| INIT/USDT:USDT | +51.74% | $3,563,759.75 |
| SSV/USDT:USDT | +33.97% | $2,235,354.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ELSA/USDT:USDT | below_1h_threshold | +4.22% | +4.18% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.22% |
| SOXL/USDT:USDT | below_1h_threshold | +0.78% | +0.74% |
| ZRO/USDT:USDT | below_1h_threshold | +0.65% | +0.61% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.64% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
