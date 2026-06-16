# Decision Report

- generated_at: 2026-06-16T01:17:47.789823+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6824**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6824, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.46% | **-1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.17% | **+0.10%** |
| LIMIT_6PCT | 4/20 | 20.0% | -0.92% | **-0.18%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.56% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.23% | **+1.90%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.63% | **+1.32%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.74** / 初期 $100.00 (+84.74%)
- 確定: 1697件 (Win 445 / Loss 528 / Flat 724) / skip 1688件
- 成長率目線: 平均log +0.000362 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUFFER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $184.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 80件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0334 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T01:17:39.333313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=66265.7
- Funnel: target 772 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +28.67% | $6,848,484.54 |
| ROAM/USDT:USDT | +25.62% | $2,679,405.47 |
| SPCXSTOCK/USDT:USDT | +22.31% | $363,674,333.95 |
| FOLKS/USDT:USDT | +20.82% | $2,532,743.18 |
| PUFFER/USDT:USDT | +20.09% | $1,163,380.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.43% | +2.36% |
| SIREN/USDT:USDT | below_1h_threshold | +2.19% | +2.11% |
| UNI/USDT:USDT | below_1h_threshold | +1.28% | +1.20% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.12% |
| COAI/USDT:USDT | below_1h_threshold | +1.13% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
