# Decision Report

- generated_at: 2026-07-15T15:01:12.971116+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8751**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=8751, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.13% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.09% | **+0.94%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.79% | **+0.81%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.60% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.92** / 初期 $100.00 (+240.92%)
- 確定: 2880件 (Win 901 / Loss 936 / Flat 1043) / skip 2432件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 0G/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $340.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 715件 (Win 167 / Loss 167 / Flat 381) / skip 1447件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.35% 残高後 $105.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 62件 (Win 19 / Loss 39 / Flat 4) / pending 2件 / skip 159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000316 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T15:01:06.722304+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=65328.1
- Funnel: target 871 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +336.63% | $31,036,448.36 |
| DODO/USDT:USDT | +42.53% | $12,909,264.42 |
| US/USDT:USDT | +39.87% | $7,205,437.05 |
| AEHRSTOCK/USDT:USDT | +29.47% | $6,523,052.87 |
| RAVE/USDT:USDT | +18.04% | $4,873,457.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CCLSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +1.89% |
| FLUTSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.85% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.71% | +1.77% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +1.10% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
