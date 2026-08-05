# Decision Report

- generated_at: 2026-08-05T18:21:35.414895+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10443**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10443, expectancy=-0.03%
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
| LIMIT_BB3S | 5/20 | 25.0% | -0.18% | **-0.04%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.60% | **-0.33%** |

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
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3234件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.28** / 初期 $100.00 (+41.28%)
- 確定: 1341件 (Win 377 / Loss 315 / Flat 649) / skip 2513件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1162 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $141.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000420 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T18:21:26.206187+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64758.4
- Funnel: target 948 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +43.70% | $37,469,745.77 |
| BLESS/USDT:USDT | +32.71% | $86,288,897.85 |
| UB/USDT:USDT | +21.75% | $23,489,029.26 |
| ESPORTS/USDT:USDT | +19.67% | $4,719,678.38 |
| HFT/USDT:USDT | +12.51% | $5,339,563.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.34% | +4.30% |
| BICO/USDT:USDT | below_1h_threshold | +3.47% | +3.43% |
| UB/USDT:USDT | below_1h_threshold | +2.21% | +2.17% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.12% | +2.08% |
| GRVT/USDT:USDT | below_1h_threshold | +1.99% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
