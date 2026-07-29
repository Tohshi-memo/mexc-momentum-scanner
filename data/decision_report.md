# Decision Report

- generated_at: 2026-07-29T10:06:31.786313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9786**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=9786, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.49%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.46% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.37% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.03% | **-0.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.32% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$119.87** / 初期 $100.00 (+19.87%)
- 確定トレード: 161件 (TP 63 / SL 93 / EXP 5)
- 最新: MUSTOCK/USDT:USDT TP_HIT PnL +7.86% 残高後 $119.87
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2828件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1970件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.16** / 初期 $100.00 (+10.16%)
- 確定: 760件 (Win 246 / Loss 291 / Flat 223) / pending 0件 / skip 499件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000514 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.16

## 6. Latest Market Context

- 更新: 2026-07-29T10:06:19.509302+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64636.9
- Funnel: target 907 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +121.05% | $2,896,403.97 |
| BEAT/USDT:USDT | +23.08% | $40,779,094.59 |
| AEON1/USDT:USDT | +19.91% | $2,124,064.49 |
| UAI/USDT:USDT | +16.94% | $1,041,711.64 |
| EUL/USDT:USDT | +16.05% | $3,142,033.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.09% | +4.13% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +4.01% | +4.04% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.03% | +3.07% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.95% | +2.99% |
| EUL/USDT:USDT | below_1h_threshold | +2.70% | +2.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
