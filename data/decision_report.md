# Decision Report

- generated_at: 2026-08-06T04:36:39.562634+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10508**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10508, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/20 | 20.0% | +5.47% | **+1.09%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.62% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.39% | **+1.36%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.68% | **+0.59%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3771件 (Win 1195 / Loss 1236 / Flat 1340) / skip 3298件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.11** / 初期 $100.00 (+40.11%)
- 確定: 1360件 (Win 379 / Loss 321 / Flat 660) / skip 2559件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $140.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 842件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000140 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T04:36:26.380091+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64659.6
- Funnel: target 949 → liquid 183 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.1 >= 65=1, 4h RSI 81.7 >= 65=1, 4h RSI 71.8 >= 65=1, 4h RSI 81.8 >= 65=1, 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +99.84% | $46,394,294.52 |
| BLESS/USDT:USDT | +55.09% | $117,385,439.23 |
| DODO/USDT:USDT | +48.84% | $7,658,479.04 |
| ESPORTS/USDT:USDT | +33.43% | $7,253,126.55 |
| BICO/USDT:USDT | +29.92% | $11,699,904.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_relative_strength | +5.04% | +4.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.75% | +3.50% |
| BTW/USDT:USDT | below_1h_threshold | +3.45% | +3.20% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.78% | +2.53% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.20% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
