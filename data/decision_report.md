# Decision Report

- generated_at: 2026-11-08T08:36:29.846254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18421**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18421, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | -0.26% | **-0.11%** |
| LIMIT_8PCT | 7/20 | 35.0% | -0.57% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.47% | **+2.26%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.00% | **+1.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.34% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,601.20** / 初期 $100.00 (+1501.20%)
- 確定: 7117件 (Win 2047 / Loss 2271 / Flat 2799) / skip 7865件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,601.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7077件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0144 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6584件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000472 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T08:36:14.636533+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=75869.3
- Funnel: target 1089 → liquid 102 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +270.67% | $11,065,253.02 |
| KOMA/USDT:USDT | +28.67% | $1,263,763.61 |
| JCT/USDT:USDT | +19.93% | $2,813,875.14 |
| ICNT/USDT:USDT | +13.64% | $3,731,939.44 |
| AIOT/USDT:USDT | +10.47% | $2,503,793.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +3.22% | +3.31% |
| AIOT/USDT:USDT | below_1h_threshold | +1.18% | +1.27% |
| MET/USDT:USDT | below_1h_threshold | +0.89% | +0.98% |
| USELESS/USDT:USDT | below_1h_threshold | +0.55% | +0.64% |
| KAS/USDT:USDT | below_1h_threshold | +0.48% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
