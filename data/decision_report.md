# Decision Report

- generated_at: 2026-08-05T15:56:41.002170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10416**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10416, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.00% | **+0.95%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.20% | **+0.36%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.30% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.18% | **+1.12%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3208件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.05** / 初期 $100.00 (+43.05%)
- 確定: 1323件 (Win 374 / Loss 311 / Flat 638) / skip 2504件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0797 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.94** / 初期 $100.00 (+17.94%)
- 確定: 1141件 (Win 365 / Loss 443 / Flat 333) / pending 1件 / skip 753件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.94

## 6. Latest Market Context

- 更新: 2026-08-05T15:56:28.992723+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64408.9
- Funnel: target 948 → liquid 184 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1, 4h RSI 80.7 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +104.22% | $31,363,729.72 |
| HFT/USDT:USDT | +76.12% | $4,804,466.36 |
| BLESS/USDT:USDT | +72.51% | $70,716,130.39 |
| CASHCAT/USDT:USDT | +38.56% | $1,023,685.83 |
| CYS/USDT:USDT | +35.79% | $32,130,233.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.26% | +4.31% |
| BASED/USDT:USDT | below_1h_threshold | +2.46% | +2.51% |
| VELVET/USDT:USDT | below_1h_threshold | +2.18% | +2.23% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |
| LAB/USDT:USDT | below_1h_threshold | +0.79% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
