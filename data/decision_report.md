# Decision Report

- generated_at: 2026-09-07T17:16:34.294569+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13897**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13897, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.16% | **+0.12%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 5/20 | 25.0% | -0.27% | **-0.07%** |
| LIMIT_BB3S | 3/19 | 15.8% | -2.29% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.12% | **+0.62%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.82% | **+0.41%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.53% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$873.98** / 初期 $100.00 (+773.98%)
- 確定: 5170件 (Win 1545 / Loss 1681 / Flat 1944) / skip 5288件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $873.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4737件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.02** / 初期 $100.00 (+20.02%)
- 確定: 2488件 (Win 732 / Loss 936 / Flat 820) / pending 3件 / skip 2876件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.02

## 6. Latest Market Context

- 更新: 2026-09-07T17:16:15.211793+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79084.8
- Funnel: target 1062 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +25.74% | $5,295,051.22 |
| BASECAT/USDT:USDT | +12.37% | $1,080,320.46 |
| BONER/USDT:USDT | +8.13% | $6,710,320.27 |
| UAI/USDT:USDT | +5.46% | $17,003,559.34 |
| ICP/USDT:USDT | +5.21% | $14,536,294.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +2.21% | +2.09% |
| ICP/USDT:USDT | below_1h_threshold | +2.15% | +2.03% |
| WLD/USDT:USDT | below_1h_threshold | +1.56% | +1.44% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.28% | +1.16% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.06% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
