# Decision Report

- generated_at: 2026-09-12T23:11:16.995399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14329**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=14329, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.81% | **+1.54%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.13%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.91% | **+0.87%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5461件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$214.54** / 初期 $100.00 (+114.54%)
- 確定: 2847件 (Win 786 / Loss 660 / Flat 1401) / skip 4893件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1507 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $214.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.71** / 初期 $100.00 (+24.71%)
- 確定: 2780件 (Win 824 / Loss 1068 / Flat 888) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000478 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $124.71

## 6. Latest Market Context

- 更新: 2026-09-12T23:11:06.433233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77237.6
- Funnel: target 1068 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +24.66% | $50,262,091.03 |
| STORJ/USDT:USDT | +21.33% | $21,940,310.77 |
| LONGXIA/USDT:USDT | +19.25% | $9,820,098.48 |
| REZ/USDT:USDT | +15.58% | $2,032,454.69 |
| ALCH/USDT:USDT | +10.79% | $2,122,720.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +3.26% | +3.21% |
| ALCH/USDT:USDT | below_1h_threshold | +2.02% | +1.97% |
| REZ/USDT:USDT | below_1h_threshold | +2.02% | +1.97% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.00% | +1.94% |
| RIVER/USDT:USDT | below_1h_threshold | +0.57% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
