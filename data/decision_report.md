# Decision Report

- generated_at: 2026-09-08T09:56:29.023277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13977**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=13977, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.06% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.34% | **+0.28%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.35% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,021.48** / 初期 $100.00 (+921.48%)
- 確定: 5245件 (Win 1583 / Loss 1703 / Flat 1959) / skip 5293件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,021.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.77** / 初期 $100.00 (+89.77%)
- 確定: 2581件 (Win 720 / Loss 620 / Flat 1241) / skip 4807件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0791 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $189.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.31** / 初期 $100.00 (+22.31%)
- 確定: 2566件 (Win 754 / Loss 962 / Flat 850) / pending 5件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000228 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $122.31

## 6. Latest Market Context

- 更新: 2026-09-08T09:56:14.045064+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=78716.4
- Funnel: target 1065 → liquid 151 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 95.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +140.84% | $15,354,174.47 |
| BNCSTOCK/USDT:USDT | +49.53% | $1,530,040.24 |
| FORM/USDT:USDT | +33.60% | $3,590,114.82 |
| USELESS/USDT:USDT | +16.35% | $11,942,575.26 |
| AERO/USDT:USDT | +15.72% | $5,910,462.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +4.90% | +4.49% |
| XPL/USDT:USDT | below_1h_threshold | +3.71% | +3.30% |
| IOST/USDT:USDT | below_1h_threshold | +3.11% | +2.70% |
| AERO/USDT:USDT | below_1h_threshold | +2.83% | +2.42% |
| ARB/USDT:USDT | below_1h_threshold | +2.54% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
