# Decision Report

- generated_at: 2026-11-03T01:56:29.967461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18045**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18045, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | +6.27% | **+1.88%** |
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.19% | **+0.90%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.21% | **+1.92%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.84% | **+1.29%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.80** / 初期 $100.00 (+1432.80%)
- 確定: 6897件 (Win 1999 / Loss 2214 / Flat 2684) / skip 7709件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,532.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.70** / 初期 $100.00 (+281.70%)
- 確定: 4482件 (Win 1204 / Loss 1000 / Flat 2278) / skip 6974件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0166 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $381.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6207件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000255 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T01:56:14.163650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77180.0
- Funnel: target 1093 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +34.86% | $18,180,730.08 |
| AGT/USDT:USDT | +17.37% | $3,060,389.06 |
| EVAA/USDT:USDT | +12.30% | $7,067,790.12 |
| JCT/USDT:USDT | +11.41% | $2,410,550.25 |
| Q/USDT:USDT | +8.17% | $6,611,970.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +4.03% | +3.93% |
| JCT/USDT:USDT | below_1h_threshold | +1.26% | +1.17% |
| BR/USDT:USDT | below_1h_threshold | +1.24% | +1.14% |
| HOT/USDT:USDT | below_1h_threshold | +0.98% | +0.88% |
| LEAD/USDT:USDT | below_1h_threshold | +0.44% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
