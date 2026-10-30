# Decision Report

- generated_at: 2026-10-30T16:46:38.983358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17857**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=17857, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.56% | **+0.90%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.09% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.87% | **+1.68%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.99% | **+1.09%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.25% | **+1.00%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.66% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6806件 (Win 1975 / Loss 2181 / Flat 2650) / skip 7612件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.04** / 初期 $100.00 (+262.04%)
- 確定: 4359件 (Win 1171 / Loss 982 / Flat 2206) / skip 6909件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0061 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $362.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6018件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000155 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T16:46:23.022565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=77461.3
- Funnel: target 1090 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +21.99% | $4,313,959.94 |
| EDGE/USDT:USDT | +3.19% | $1,486,344.31 |
| BIRB/USDT:USDT | +2.91% | $1,493,836.62 |
| RUNE/USDT:USDT | +1.63% | $2,950,787.80 |
| GRASS/USDT:USDT | +1.51% | $1,667,188.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.20% | +3.35% |
| BIRB/USDT:USDT | below_1h_threshold | +2.64% | +2.80% |
| SOXS/USDT:USDT | below_1h_threshold | +1.82% | +1.98% |
| RUNE/USDT:USDT | below_1h_threshold | +1.54% | +1.69% |
| GRASS/USDT:USDT | below_1h_threshold | +1.52% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
