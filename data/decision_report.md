# Decision Report

- generated_at: 2026-06-18T04:03:07.291761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7001**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7001, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.36% | **+0.11%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.16% | **-0.06%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.42% | **-0.11%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_8PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.65% | **+2.65%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.13** / 初期 $100.00 (+115.13%)
- 確定: 1847件 (Win 514 / Loss 582 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $215.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.32** / 初期 $100.00 (+5.32%)
- 確定: 274件 (Win 75 / Loss 70 / Flat 129) / skip 138件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0661 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $105.32

## 5. Latest Market Context

- 更新: 2026-06-18T04:03:03.005921+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64285.0
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +127.04% | $33,707,527.29 |
| O/USDT:USDT | +60.13% | $1,961,907.94 |
| SYN/USDT:USDT | +49.17% | $4,559,055.19 |
| HOME/USDT:USDT | +39.22% | $1,190,961.90 |
| H/USDT:USDT | +25.89% | $33,404,505.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.54% | +3.49% |
| BEAT/USDT:USDT | below_1h_threshold | +0.90% | +0.85% |
| BASED/USDT:USDT | below_1h_threshold | +0.72% | +0.67% |
| AGT/USDT:USDT | below_1h_threshold | +0.65% | +0.60% |
| PLAY/USDT:USDT | below_1h_threshold | +0.60% | +0.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
