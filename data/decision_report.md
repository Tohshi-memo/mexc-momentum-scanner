# Decision Report

- generated_at: 2026-11-21T17:51:37.546694+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19327**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=19327, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.99% | **+1.89%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.99% | **+0.84%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_BB3S | 5/11 | 45.5% | +1.50% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.97% | **+1.78%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.44% | **+1.46%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.15% | **+1.45%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.75% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,735.92** / 初期 $100.00 (+1635.92%)
- 確定: 7470件 (Win 2144 / Loss 2403 / Flat 2923) / skip 8418件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,735.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.22** / 初期 $100.00 (+348.22%)
- 確定: 5124件 (Win 1363 / Loss 1100 / Flat 2661) / skip 7614件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $448.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7490件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T17:51:19.288256+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=59975.9
- Funnel: target 1086 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +30.82% | $1,846,344.51 |
| PIEVERSE/USDT:USDT | +12.38% | $4,999,951.95 |
| NIGHT/USDT:USDT | +6.68% | $1,158,513.66 |
| BLESS/USDT:USDT | +5.51% | $54,206,046.46 |
| DODO/USDT:USDT | +5.33% | $1,517,831.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.44% | +4.53% |
| TIA/USDT:USDT | below_1h_threshold | +1.86% | +1.96% |
| IDOL/USDT:USDT | below_1h_threshold | +1.47% | +1.57% |
| LUNC/USDT:USDT | below_1h_threshold | +1.28% | +1.38% |
| EVAA/USDT:USDT | below_1h_threshold | +1.23% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
