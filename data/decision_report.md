# Decision Report

- generated_at: 2026-07-12T04:51:10.200927+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8570**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8570, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.04% | **+0.40%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.04% | **+0.03%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.23% | **-0.05%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.20% | **-0.10%** |
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.72% | **+1.29%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.08% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.70% | **+0.34%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.54** / 初期 $100.00 (+2.54%)
- 確定トレード: 86件 (TP 30 / SL 55 / EXP 1)
- 最新: ELSA/USDT:USDT SL_HIT PnL -3.75% 残高後 $102.54
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.13** / 初期 $100.00 (+219.13%)
- 確定: 2758件 (Win 869 / Loss 921 / Flat 968) / skip 2373件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $319.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1338件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0067 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 17件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T04:51:03.929116+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=63960.1
- Funnel: target 863 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +24.89% | $14,874,474.48 |
| B/USDT:USDT | +18.19% | $50,245,559.87 |
| CASHCAT/USDT:USDT | +18.02% | $2,178,425.71 |
| ELSA/USDT:USDT | +12.91% | $1,224,430.30 |
| T/USDT:USDT | +10.48% | $14,487,579.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPIN/USDT:USDT | below_1h_threshold | +3.03% | +3.40% |
| BASED/USDT:USDT | below_1h_threshold | +2.30% | +2.67% |
| EDGE/USDT:USDT | below_1h_threshold | +2.09% | +2.47% |
| US/USDT:USDT | below_1h_threshold | +1.71% | +2.09% |
| ELSA/USDT:USDT | below_1h_threshold | +1.47% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
