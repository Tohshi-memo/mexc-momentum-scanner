# Decision Report

- generated_at: 2026-08-05T19:16:29.707994+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10447**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10447, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.43% | **-0.19%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.70% | **-0.31%** |
| LIMIT_6PCT | 6/20 | 30.0% | -1.06% | **-0.32%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.49% | **-0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.73% | **+2.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.11% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3238件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.78** / 初期 $100.00 (+40.78%)
- 確定: 1345件 (Win 377 / Loss 316 / Flat 652) / skip 2513件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $140.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000571 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T19:16:19.880209+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=64854.5
- Funnel: target 948 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +48.19% | $91,285,946.57 |
| HEI/USDT:USDT | +47.36% | $40,283,125.61 |
| UB/USDT:USDT | +23.13% | $22,670,345.19 |
| ESPORTS/USDT:USDT | +21.92% | $4,877,767.56 |
| BICO/USDT:USDT | +13.85% | $13,456,111.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.76% | +4.62% |
| SYN/USDT:USDT | below_1h_threshold | +4.17% | +4.03% |
| UB/USDT:USDT | below_1h_threshold | +2.05% | +1.91% |
| CYS/USDT:USDT | below_1h_threshold | +1.10% | +0.96% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.81% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
