# Decision Report

- generated_at: 2026-10-19T18:31:24.992574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17021**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=17021, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.42% | **+0.33%** |
| LIMIT_BB3S | 2/13 | 15.4% | -0.98% | **-0.15%** |
| LIMIT_5PCT | 2/20 | 10.0% | -1.52% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.71% | **+0.53%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.59% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,270.80** / 初期 $100.00 (+1170.80%)
- 確定: 6466件 (Win 1876 / Loss 2064 / Flat 2526) / skip 7116件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.00% 残高後 $1,270.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3786件 (Win 1041 / Loss 885 / Flat 1860) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0287 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.02% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5182件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T18:31:11.203190+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=81831.9
- Funnel: target 1090 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +18.09% | $2,332,294.36 |
| APR/USDT:USDT | +11.50% | $1,501,883.77 |
| BTW/USDT:USDT | +7.38% | $24,533,401.39 |
| SOXS/USDT:USDT | +6.33% | $3,175,759.71 |
| CLAUDIA/USDT:USDT | +6.01% | $1,035,944.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.60% | +3.68% |
| PHA/USDT:USDT | below_1h_threshold | +3.52% | +3.60% |
| S/USDT:USDT | below_1h_threshold | +2.34% | +2.42% |
| Q/USDT:USDT | below_1h_threshold | +1.54% | +1.62% |
| SOXS/USDT:USDT | below_1h_threshold | +1.49% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
