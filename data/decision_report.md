# Decision Report

- generated_at: 2026-07-14T04:21:09.483986+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8664**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8664, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.51% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.60% | **+1.04%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.16** / 初期 $100.00 (+229.16%)
- 確定: 2832件 (Win 889 / Loss 924 / Flat 1019) / skip 2393件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $329.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.75** / 初期 $100.00 (+4.75%)
- 確定: 664件 (Win 157 / Loss 161 / Flat 346) / skip 1411件
- 成長率目線: 平均log +0.000070 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0547 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $104.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.46** / 初期 $100.00 (-0.54%)
- 確定: 45件 (Win 16 / Loss 29 / Flat 0) / pending 3件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000328 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.46

## 6. Latest Market Context

- 更新: 2026-07-14T04:21:03.108848+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62573.1
- Funnel: target 867 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +33.65% | $7,112,503.45 |
| ZBT/USDT:USDT | +23.62% | $2,364,962.03 |
| TRIA/USDT:USDT | +20.68% | $1,506,726.80 |
| LAB/USDT:USDT | +20.24% | $14,580,047.75 |
| EVAA/USDT:USDT | +15.96% | $21,888,855.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.23% | +4.18% |
| VELVET/USDT:USDT | below_1h_threshold | +2.65% | +2.59% |
| ZBT/USDT:USDT | below_1h_threshold | +2.53% | +2.47% |
| BSB/USDT:USDT | below_1h_threshold | +2.08% | +2.03% |
| BLAST/USDT:USDT | below_1h_threshold | +1.59% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
