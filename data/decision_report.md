# Decision Report

- generated_at: 2026-08-05T18:16:27.272902+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10442**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10442, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 4/20 | 20.0% | -0.39% | **-0.08%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.55% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.81% | **+2.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.09% | **+2.63%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.03% | **+2.21%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.73% | **+0.43%** |
| LIMIT_6PCT_LONG | 3/20 | 15.0% | +1.25% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3233件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.28** / 初期 $100.00 (+41.28%)
- 確定: 1340件 (Win 377 / Loss 315 / Flat 648) / skip 2513件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1066 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 776件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000401 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T18:16:18.029605+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64784.7
- Funnel: target 948 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +39.28% | $36,939,993.49 |
| BLESS/USDT:USDT | +29.04% | $85,758,502.21 |
| UB/USDT:USDT | +20.59% | $23,377,886.82 |
| ESPORTS/USDT:USDT | +18.69% | $4,701,624.70 |
| HFT/USDT:USDT | +10.65% | $5,303,925.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +2.34% | +2.26% |
| HFT/USDT:USDT | below_1h_threshold | +2.20% | +2.12% |
| SHOPSTOCK/USDT:USDT | below_1h_threshold | +1.60% | +1.53% |
| BTW/USDT:USDT | below_1h_threshold | +1.41% | +1.33% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.36% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
