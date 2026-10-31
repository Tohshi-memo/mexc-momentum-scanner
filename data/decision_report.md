# Decision Report

- generated_at: 2026-10-31T03:11:23.747505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17880**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=17880, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.78% | **+0.58%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.55% | **+0.49%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.10** / 初期 $100.00 (+1431.10%)
- 確定: 6810件 (Win 1976 / Loss 2182 / Flat 2652) / skip 7631件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,531.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$366.27** / 初期 $100.00 (+266.27%)
- 確定: 4380件 (Win 1178 / Loss 983 / Flat 2219) / skip 6911件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0495 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $366.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6044件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T03:11:10.887395+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=77284.4
- Funnel: target 1090 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +51.40% | $7,401,949.67 |
| SOPH/USDT:USDT | +24.12% | $1,391,501.45 |
| IDOL/USDT:USDT | +23.14% | $14,477,197.77 |
| LSK/USDT:USDT | +11.72% | $4,861,076.66 |
| OP/USDT:USDT | +9.71% | $16,285,651.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOPH/USDT:USDT | below_1h_threshold | +2.87% | +3.03% |
| AIN/USDT:USDT | below_1h_threshold | +2.35% | +2.50% |
| LSK/USDT:USDT | below_1h_threshold | +0.76% | +0.91% |
| OP/USDT:USDT | below_1h_threshold | +0.57% | +0.72% |
| XPL/USDT:USDT | below_1h_threshold | +0.44% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
