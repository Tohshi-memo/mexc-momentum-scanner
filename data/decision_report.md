# Decision Report

- generated_at: 2026-09-07T19:46:16.540293+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13902**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13902, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 5/20 | 25.0% | +1.53% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.14% | **+0.01%** |
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.29% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.36% | **+0.61%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$873.91** / 初期 $100.00 (+773.91%)
- 確定: 5175件 (Win 1546 / Loss 1683 / Flat 1946) / skip 5288件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $873.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4741件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.01** / 初期 $100.00 (+20.01%)
- 確定: 2493件 (Win 733 / Loss 938 / Flat 822) / pending 3件 / skip 2876件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.01

## 6. Latest Market Context

- 更新: 2026-09-07T19:46:04.672765+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=79307.3
- Funnel: target 1062 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +18.20% | $5,838,356.00 |
| AERO/USDT:USDT | +11.94% | $2,276,326.18 |
| BONER/USDT:USDT | +10.29% | $6,955,404.73 |
| INJ/USDT:USDT | +9.06% | $24,231,466.46 |
| BASECAT/USDT:USDT | +8.59% | $1,106,373.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +4.07% | +3.88% |
| CHIP/USDT:USDT | below_1h_threshold | +3.59% | +3.40% |
| SOPH/USDT:USDT | below_1h_threshold | +3.58% | +3.39% |
| AERO/USDT:USDT | below_1h_threshold | +3.14% | +2.96% |
| INJ/USDT:USDT | below_1h_threshold | +2.90% | +2.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
