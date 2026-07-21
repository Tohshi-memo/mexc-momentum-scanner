# Decision Report

- generated_at: 2026-07-21T15:41:17.944403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9189**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9189, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.30% | **+1.24%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.44% | **+0.42%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.02% | **+1.81%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.49% | **+0.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.66% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2501件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.69** / 初期 $100.00 (+32.69%)
- 確定: 1150件 (Win 311 / Loss 247 / Flat 592) / skip 1450件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0734 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $132.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定: 346件 (Win 121 / Loss 153 / Flat 72) / pending 3件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.99

## 6. Latest Market Context

- 更新: 2026-07-21T15:41:10.087285+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=66596.8
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +113.30% | $5,175,653.55 |
| PONS/USDT:USDT | +90.82% | $1,423,593.64 |
| ERA/USDT:USDT | +63.66% | $12,569,416.80 |
| ESPORTS/USDT:USDT | +51.56% | $8,701,363.36 |
| ONE/USDT:USDT | +39.68% | $2,419,001.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.28% | +4.60% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +3.19% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.46% | +2.77% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.59% |
| KORU/USDT:USDT | below_1h_threshold | +2.22% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
