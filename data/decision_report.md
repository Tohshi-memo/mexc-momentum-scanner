# Decision Report

- generated_at: 2026-07-14T05:16:15.900135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8669**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8669, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.95% | **+1.27%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.45% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.95% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.71** / 初期 $100.00 (+230.71%)
- 確定: 2837件 (Win 891 / Loss 924 / Flat 1022) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $330.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.91** / 初期 $100.00 (+4.91%)
- 確定: 668件 (Win 158 / Loss 161 / Flat 349) / skip 1412件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0509 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $104.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.62** / 初期 $100.00 (-0.38%)
- 確定: 50件 (Win 18 / Loss 32 / Flat 0) / pending 4件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.62

## 6. Latest Market Context

- 更新: 2026-07-14T05:16:07.530120+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=62795.3
- Funnel: target 867 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +33.69% | $7,107,460.76 |
| ZBT/USDT:USDT | +23.70% | $2,671,616.25 |
| TRIA/USDT:USDT | +16.77% | $1,638,344.41 |
| EVAA/USDT:USDT | +14.53% | $21,702,592.31 |
| FOLKS/USDT:USDT | +9.33% | $1,305,174.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.67% | +4.55% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.49% | +3.36% |
| DRAM/USDT:USDT | below_1h_threshold | +2.99% | +2.87% |
| SXT/USDT:USDT | below_1h_threshold | +2.76% | +2.63% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.45% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
