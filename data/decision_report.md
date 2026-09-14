# Decision Report

- generated_at: 2026-09-14T16:16:30.651033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14525**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=14525, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.96% | **+1.86%** |
| LIMIT_3PCT | 15/20 | 75.0% | +2.01% | **+1.51%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.66% | **+1.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.15% | **+0.10%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.65% | **-0.07%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.14% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,052.44** / 初期 $100.00 (+952.44%)
- 確定: 5445件 (Win 1637 / Loss 1770 / Flat 2038) / skip 5641件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2992件 (Win 830 / Loss 716 / Flat 1446) / skip 4944件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0048 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.54** / 初期 $100.00 (+25.54%)
- 確定: 2890件 (Win 859 / Loss 1120 / Flat 911) / pending 0件 / skip 3105件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000077 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.54

## 6. Latest Market Context

- 更新: 2026-09-14T16:16:20.089348+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78523.4
- Funnel: target 1073 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +7.21% | $2,358,706.23 |
| AIN/USDT:USDT | +4.98% | $4,506,065.67 |
| KOMA/USDT:USDT | +2.78% | $1,154,414.09 |
| 4/USDT:USDT | +2.37% | $1,387,319.78 |
| NEAR/USDT:USDT | +1.25% | $31,422,592.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +4.93% | +4.95% |
| KORU/USDT:USDT | below_1h_threshold | +3.51% | +3.53% |
| KOMA/USDT:USDT | below_1h_threshold | +2.79% | +2.81% |
| LSK/USDT:USDT | below_1h_threshold | +2.74% | +2.76% |
| 4/USDT:USDT | below_1h_threshold | +2.38% | +2.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
