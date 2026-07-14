# Decision Report

- generated_at: 2026-07-14T05:46:16.136061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8672**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8672, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.11% | **+1.06%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.10% | **+0.95%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.71** / 初期 $100.00 (+230.71%)
- 確定: 2840件 (Win 891 / Loss 924 / Flat 1025) / skip 2393件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $330.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.98** / 初期 $100.00 (+4.98%)
- 確定: 671件 (Win 159 / Loss 161 / Flat 351) / skip 1412件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0520 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $104.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.62** / 初期 $100.00 (-0.38%)
- 確定: 53件 (Win 19 / Loss 34 / Flat 0) / pending 3件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.62

## 6. Latest Market Context

- 更新: 2026-07-14T05:46:08.634463+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62710.0
- Funnel: target 867 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +28.75% | $7,239,568.95 |
| TRIA/USDT:USDT | +27.11% | $1,870,024.01 |
| ZBT/USDT:USDT | +23.28% | $2,797,373.83 |
| EVAA/USDT:USDT | +14.04% | $21,842,074.74 |
| VELVET/USDT:USDT | +11.12% | $33,655,515.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.67% | +4.68% |
| BSB/USDT:USDT | below_1h_threshold | +4.29% | +4.30% |
| SXT/USDT:USDT | below_1h_threshold | +3.79% | +3.80% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.49% | +3.50% |
| DRAM/USDT:USDT | below_1h_threshold | +2.99% | +3.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
