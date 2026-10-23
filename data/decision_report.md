# Decision Report

- generated_at: 2026-10-23T04:46:34.033940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17189**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17189, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.16% | **-0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.70% | **+1.67%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.63%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.84% | **+0.50%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.81% | **+0.36%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.20% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,317.51** / 初期 $100.00 (+1217.51%)
- 確定: 6545件 (Win 1900 / Loss 2089 / Flat 2556) / skip 7205件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,317.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.12** / 初期 $100.00 (+177.12%)
- 確定: 3865件 (Win 1057 / Loss 900 / Flat 1908) / skip 6735件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $277.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5352件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T04:46:16.464891+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=81650.9
- Funnel: target 1096 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +41.37% | $13,170,283.47 |
| IRYS/USDT:USDT | +24.84% | $3,828,409.77 |
| AGT/USDT:USDT | +17.71% | $6,235,377.33 |
| AKE/USDT:USDT | +14.92% | $12,241,642.53 |
| DNA/USDT:USDT | +13.75% | $4,252,575.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.68% | +3.94% |
| BR/USDT:USDT | below_1h_threshold | +3.57% | +3.83% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.12% | +2.38% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.85% | +2.11% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.83% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
