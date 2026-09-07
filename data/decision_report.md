# Decision Report

- generated_at: 2026-09-07T22:46:22.114190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13919**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13919, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.25% | **-2.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.35% | **+0.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.91% | **+3.13%** |
| MARKET_LONG | 20/20 | 100.0% | +2.99% | **+2.99%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +4.02% | **+2.01%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.63% | **+0.92%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$954.08** / 初期 $100.00 (+854.08%)
- 確定: 5192件 (Win 1559 / Loss 1684 / Flat 1949) / skip 5288件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $954.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4758件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.97** / 初期 $100.00 (+21.97%)
- 確定: 2509件 (Win 740 / Loss 940 / Flat 829) / pending 6件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $121.97

## 6. Latest Market Context

- 更新: 2026-09-07T22:46:07.779773+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=78820.9
- Funnel: target 1062 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +49.46% | $5,729,227.66 |
| BONER/USDT:USDT | +18.79% | $5,629,990.93 |
| SOPH/USDT:USDT | +16.64% | $1,731,388.43 |
| AERO/USDT:USDT | +12.23% | $3,696,195.97 |
| INJ/USDT:USDT | +7.05% | $43,126,272.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +3.91% | +4.30% |
| SOPH/USDT:USDT | below_1h_threshold | +3.46% | +3.84% |
| XAN/USDT:USDT | below_1h_threshold | +2.99% | +3.38% |
| UAI/USDT:USDT | below_1h_threshold | +1.60% | +1.99% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.54% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
