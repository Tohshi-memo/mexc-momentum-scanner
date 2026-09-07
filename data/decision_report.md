# Decision Report

- generated_at: 2026-09-07T22:26:29.814213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13915**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13915, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.55% | **+0.27%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.27% | **+2.78%** |
| MARKET_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.72%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +5.33% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$929.42** / 初期 $100.00 (+829.42%)
- 確定: 5188件 (Win 1556 / Loss 1684 / Flat 1948) / skip 5288件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $929.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4754件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定: 2505件 (Win 738 / Loss 940 / Flat 827) / pending 5件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000300 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.13

## 6. Latest Market Context

- 更新: 2026-09-07T22:26:15.679571+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=79129.7
- Funnel: target 1062 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +23.35% | $5,530,602.02 |
| BONER/USDT:USDT | +20.06% | $5,590,488.86 |
| SOPH/USDT:USDT | +15.50% | $1,713,065.51 |
| AERO/USDT:USDT | +13.18% | $3,600,252.28 |
| BR/USDT:USDT | +9.00% | $1,425,763.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +3.76% | +3.75% |
| XAN/USDT:USDT | below_1h_threshold | +2.42% | +2.42% |
| SOPH/USDT:USDT | below_1h_threshold | +2.32% | +2.31% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.84% | +1.84% |
| CHIP/USDT:USDT | below_1h_threshold | +1.46% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
