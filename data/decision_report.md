# Decision Report

- generated_at: 2026-07-21T15:51:19.905859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9190**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9190, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.25% | **+1.19%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.44% | **+0.42%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.28% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.77% | **+1.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.49% | **+0.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.82% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2502件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$133.60** / 初期 $100.00 (+33.60%)
- 確定: 1151件 (Win 312 / Loss 247 / Flat 592) / skip 1450件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0786 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $133.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定: 347件 (Win 122 / Loss 153 / Flat 72) / pending 3件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $101.34

## 6. Latest Market Context

- 更新: 2026-07-21T15:51:13.104398+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=66658.4
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +115.67% | $5,229,116.13 |
| PONS/USDT:USDT | +96.09% | $1,439,638.56 |
| ERA/USDT:USDT | +63.11% | $12,598,910.45 |
| ESPORTS/USDT:USDT | +54.12% | $9,027,678.21 |
| ONE/USDT:USDT | +34.83% | $2,510,562.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.28% | +4.50% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.71% | +3.93% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +3.09% |
| MUU/USDT:USDT | below_1h_threshold | +2.63% | +2.85% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
