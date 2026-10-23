# Decision Report

- generated_at: 2026-10-23T04:36:27.943080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17188**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17188, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.80% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.93% | **+1.47%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.78% | **+0.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.47% | **+0.30%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.41% | **+0.21%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,324.13** / 初期 $100.00 (+1224.13%)
- 確定: 6544件 (Win 1900 / Loss 2088 / Flat 2556) / skip 7205件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,324.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.12** / 初期 $100.00 (+177.12%)
- 確定: 3864件 (Win 1057 / Loss 900 / Flat 1907) / skip 6735件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $277.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5349件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T04:36:13.432698+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=81649.8
- Funnel: target 1096 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +37.92% | $13,073,561.29 |
| IRYS/USDT:USDT | +20.96% | $3,787,722.80 |
| AGT/USDT:USDT | +20.64% | $6,136,101.92 |
| DNA/USDT:USDT | +13.98% | $4,249,814.27 |
| GTC/USDT:USDT | +10.27% | $1,151,916.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.87% | +4.13% |
| IRYS/USDT:USDT | below_1h_threshold | +2.38% | +2.64% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.12% | +2.38% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.85% | +2.11% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.83% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
