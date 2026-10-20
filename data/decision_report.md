# Decision Report

- generated_at: 2026-10-20T12:31:31.552175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17062**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17062, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.59% | **+0.15%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.20% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +2.90% | **+2.90%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.10% | **+1.37%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.67% | **+1.34%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.49% | **+0.82%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.36% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 247件 (TP 91 / SL 149 / EXP 7)
- 最新: BAT/USDT:USDT SL_HIT PnL -3.97% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,330.95** / 初期 $100.00 (+1230.95%)
- 確定: 6482件 (Win 1886 / Loss 2068 / Flat 2528) / skip 7141件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.52% 残高後 $1,330.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$283.11** / 初期 $100.00 (+183.11%)
- 確定: 3810件 (Win 1049 / Loss 887 / Flat 1874) / skip 6663件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0814 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $283.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5221件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T12:31:19.655319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81500.0
- Funnel: target 1083 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +121.71% | $14,705,429.75 |
| APR/USDT:USDT | +31.04% | $1,091,760.24 |
| ALT/USDT:USDT | +21.42% | $2,327,154.30 |
| PHA/USDT:USDT | +15.05% | $19,858,122.64 |
| SOXS/USDT:USDT | +12.52% | $3,936,909.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.22% | +4.18% |
| S/USDT:USDT | below_1h_threshold | +1.62% | +1.58% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.54% | +1.50% |
| RLC/USDT:USDT | below_1h_threshold | +1.51% | +1.47% |
| USELESS/USDT:USDT | below_1h_threshold | +1.38% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
