# Decision Report

- generated_at: 2026-10-04T06:56:23.999556+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16098, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.34% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.02% | **+1.92%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.81% | **+1.81%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,288.46** / 初期 $100.00 (+1188.46%)
- 確定: 6158件 (Win 1814 / Loss 1974 / Flat 2370) / skip 6501件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,288.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3608件 (Win 1005 / Loss 845 / Flat 1758) / skip 5901件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4259件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T06:56:11.992097+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=85017.0
- Funnel: target 1086 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +23.41% | $1,232,958.22 |
| SPORTFUN/USDT:USDT | +18.82% | $1,768,371.88 |
| AXS/USDT:USDT | +18.69% | $5,006,698.71 |
| ATH/USDT:USDT | +16.69% | $4,053,472.20 |
| AIN/USDT:USDT | +12.96% | $5,736,071.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +4.14% | +3.97% |
| NIL/USDT:USDT | below_1h_threshold | +3.00% | +2.83% |
| GALA/USDT:USDT | below_1h_threshold | +2.71% | +2.54% |
| ATOM/USDT:USDT | below_1h_threshold | +2.39% | +2.23% |
| APE/USDT:USDT | below_1h_threshold | +1.80% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
