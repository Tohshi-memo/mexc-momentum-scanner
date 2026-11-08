# Decision Report

- generated_at: 2026-11-08T06:11:26.883031+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18407**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18407, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 11/20 | 55.0% | +1.43% | **+0.79%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.50% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +3.68% | **+2.95%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +2.73% | **+2.46%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.00% | **+2.40%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.12% | **+2.01%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.83% | **+1.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,554.23** / 初期 $100.00 (+1454.23%)
- 確定: 7103件 (Win 2043 / Loss 2269 / Flat 2791) / skip 7865件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,554.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7063件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6567件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000419 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T06:11:10.940981+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=75766.9
- Funnel: target 1089 → liquid 106 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +167.47% | $8,099,374.71 |
| MET/USDT:USDT | +6.32% | $1,637,628.51 |
| BTW/USDT:USDT | +4.50% | $6,189,471.55 |
| ESPORTS/USDT:USDT | +3.96% | $1,263,762.04 |
| AIOT/USDT:USDT | +3.94% | $2,222,848.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +2.09% | +2.13% |
| MET/USDT:USDT | below_1h_threshold | +0.89% | +0.93% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.89% | +0.93% |
| MUU/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |
| ARIA/USDT:USDT | below_1h_threshold | +0.79% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
