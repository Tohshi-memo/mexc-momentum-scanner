# Decision Report

- generated_at: 2026-07-21T16:16:20.735403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9193**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=9193, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.21% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S | 4/17 | 23.5% | +2.80% | **+0.66%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.89% | **+0.95%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2505件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.20** / 初期 $100.00 (+32.20%)
- 確定: 1154件 (Win 312 / Loss 250 / Flat 592) / skip 1450件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0328 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $132.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.98** / 初期 $100.00 (+0.98%)
- 確定: 349件 (Win 122 / Loss 155 / Flat 72) / pending 2件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $100.98

## 6. Latest Market Context

- 更新: 2026-07-21T16:16:13.854260+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=66567.4
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +7.52% | $2,939,765.88 |
| BILL/USDT:USDT | +3.42% | $2,082,148.51 |
| MUU/USDT:USDT | +3.12% | $1,092,634.51 |
| BULLA/USDT:USDT | +2.84% | $1,421,700.07 |
| RE/USDT:USDT | +2.78% | $1,138,411.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.43% | +3.55% |
| RE/USDT:USDT | below_1h_threshold | +3.14% | +3.26% |
| BULLA/USDT:USDT | below_1h_threshold | +3.11% | +3.23% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.51% |
| BANK/USDT:USDT | below_1h_threshold | +2.07% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
