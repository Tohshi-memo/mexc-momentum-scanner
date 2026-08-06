# Decision Report

- generated_at: 2026-08-06T06:41:35.452947+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10538, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_7PCT | 8/20 | 40.0% | +4.55% | **+1.82%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.28% | **+6.28%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.26% | **+2.93%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.78% | **+1.95%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.28% | **+1.80%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.73% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3771件 (Win 1195 / Loss 1236 / Flat 1340) / skip 3328件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.11** / 初期 $100.00 (+40.11%)
- 確定: 1374件 (Win 379 / Loss 321 / Flat 674) / skip 2575件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1388 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $140.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 865件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T06:41:26.025893+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64785.4
- Funnel: target 952 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +137.83% | $54,926,184.18 |
| DODO/USDT:USDT | +59.43% | $8,913,243.53 |
| BLESS/USDT:USDT | +44.70% | $122,735,850.45 |
| CASHCAT/USDT:USDT | +28.77% | $1,253,917.60 |
| BICO/USDT:USDT | +28.02% | $10,942,102.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.72% | +4.86% |
| UB/USDT:USDT | below_1h_threshold | +4.01% | +4.16% |
| BTW/USDT:USDT | below_1h_threshold | +3.44% | +3.58% |
| MMT/USDT:USDT | below_1h_threshold | +2.34% | +2.48% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.02% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
