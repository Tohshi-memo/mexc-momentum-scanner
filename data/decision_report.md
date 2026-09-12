# Decision Report

- generated_at: 2026-09-12T23:41:23.548902+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14331**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=14331, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.27% | **+1.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.92% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.66% | **+1.32%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.22% | **+1.16%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.41%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5462件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$216.01** / 初期 $100.00 (+116.01%)
- 確定: 2849件 (Win 787 / Loss 660 / Flat 1402) / skip 4893件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1492 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $216.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.13** / 初期 $100.00 (+25.13%)
- 確定: 2782件 (Win 825 / Loss 1068 / Flat 889) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000493 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $125.13

## 6. Latest Market Context

- 更新: 2026-09-12T23:41:12.635720+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77214.9
- Funnel: target 1068 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.0 >= 65=1, 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +33.05% | $53,112,338.82 |
| STORJ/USDT:USDT | +23.15% | $22,086,407.22 |
| REZ/USDT:USDT | +17.51% | $2,179,889.14 |
| LONGXIA/USDT:USDT | +16.57% | $9,881,816.23 |
| ALCH/USDT:USDT | +14.27% | $2,238,642.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REZ/USDT:USDT | below_1h_threshold | +3.67% | +3.64% |
| VTHO/USDT:USDT | below_1h_threshold | +2.44% | +2.41% |
| ILV/USDT:USDT | below_1h_threshold | +1.98% | +1.95% |
| RIVER/USDT:USDT | below_1h_threshold | +1.15% | +1.12% |
| PEPE/USDT:USDT | below_1h_threshold | +0.49% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
