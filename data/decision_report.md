# Decision Report

- generated_at: 2026-10-18T05:21:17.576115+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16942**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=16942, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.71% | **+1.30%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.13% | **+0.91%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.37% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,278.09** / 初期 $100.00 (+1178.09%)
- 確定: 6408件 (Win 1865 / Loss 2051 / Flat 2492) / skip 7095件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,278.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.01** / 初期 $100.00 (+177.01%)
- 確定: 3707件 (Win 1031 / Loss 880 / Flat 1796) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0133 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5103件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T05:21:06.001753+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81803.7
- Funnel: target 1084 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +25.17% | $9,355,403.27 |
| CLAUDIA/USDT:USDT | +18.00% | $2,413,381.51 |
| AVA/USDT:USDT | +15.45% | $2,505,223.72 |
| BR/USDT:USDT | +13.71% | $11,104,018.77 |
| XMR/USDT:USDT | +9.51% | $7,412,617.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +4.72% | +4.67% |
| BTW/USDT:USDT | below_1h_threshold | +2.10% | +2.06% |
| AGT/USDT:USDT | below_1h_threshold | +1.78% | +1.73% |
| BR/USDT:USDT | below_1h_threshold | +1.31% | +1.27% |
| SAND/USDT:USDT | below_1h_threshold | +1.06% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
