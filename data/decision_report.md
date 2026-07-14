# Decision Report

- generated_at: 2026-07-14T04:46:10.271358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8666**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=8666, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.54% | **+1.08%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.79% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.93** / 初期 $100.00 (+229.93%)
- 確定: 2834件 (Win 890 / Loss 924 / Flat 1020) / skip 2393件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $329.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.75** / 初期 $100.00 (+4.75%)
- 確定: 665件 (Win 157 / Loss 161 / Flat 347) / skip 1412件
- 成長率目線: 平均log +0.000070 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0505 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $104.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.12** / 初期 $100.00 (-0.88%)
- 確定: 47件 (Win 16 / Loss 31 / Flat 0) / pending 3件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.12

## 6. Latest Market Context

- 更新: 2026-07-14T04:46:02.660443+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=62687.9
- Funnel: target 867 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +33.87% | $15,865,513.94 |
| AIOT/USDT:USDT | +32.35% | $7,192,369.51 |
| ZBT/USDT:USDT | +23.28% | $2,525,141.70 |
| TRIA/USDT:USDT | +16.89% | $1,604,513.86 |
| EVAA/USDT:USDT | +15.85% | $22,032,072.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.79% | +4.55% |
| AIOT/USDT:USDT | below_1h_threshold | +3.22% | +2.98% |
| INJ/USDT:USDT | below_1h_threshold | +2.62% | +2.38% |
| BSB/USDT:USDT | below_1h_threshold | +2.40% | +2.16% |
| ZBT/USDT:USDT | below_1h_threshold | +2.25% | +2.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
