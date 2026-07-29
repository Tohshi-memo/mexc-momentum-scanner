# Decision Report

- generated_at: 2026-07-29T08:06:22.526344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9780**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=9780, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.21% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.45% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$119.87** / 初期 $100.00 (+19.87%)
- 確定トレード: 161件 (TP 63 / SL 93 / EXP 5)
- 最新: MUSTOCK/USDT:USDT TP_HIT PnL +7.86% 残高後 $119.87
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2822件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1964件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0241 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.16** / 初期 $100.00 (+10.16%)
- 確定: 760件 (Win 246 / Loss 291 / Flat 223) / pending 0件 / skip 491件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000537 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.16

## 6. Latest Market Context

- 更新: 2026-07-29T08:06:15.423552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64470.5
- Funnel: target 907 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +130.99% | $2,277,831.72 |
| AEON1/USDT:USDT | +21.79% | $1,930,476.02 |
| BEAT/USDT:USDT | +20.82% | $43,261,323.41 |
| BTW/USDT:USDT | +15.85% | $8,112,131.57 |
| ZIL/USDT:USDT | +11.53% | $9,832,523.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.36% | +4.46% |
| AEON1/USDT:USDT | below_1h_threshold | +1.85% | +1.95% |
| SOXS/USDT:USDT | below_1h_threshold | +1.26% | +1.36% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.09% | +1.18% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.80% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
