# Decision Report

- generated_at: 2026-09-22T02:51:31.143266+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15290**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=15290, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.96% | **+1.77%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_BB3S | 8/16 | 50.0% | +1.71% | **+0.86%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.93% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,180.25** / 初期 $100.00 (+1080.25%)
- 確定: 5781件 (Win 1720 / Loss 1860 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,180.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.16** / 初期 $100.00 (+149.16%)
- 確定: 3329件 (Win 920 / Loss 771 / Flat 1638) / skip 5372件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $249.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.87** / 初期 $100.00 (+22.87%)
- 確定: 3062件 (Win 901 / Loss 1198 / Flat 963) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.87

## 6. Latest Market Context

- 更新: 2026-09-22T02:51:17.456515+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=85750.0
- Funnel: target 1055 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.2 >= 65=1, 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +37.89% | $2,411,323.21 |
| FORM/USDT:USDT | +22.74% | $9,111,155.81 |
| ALCH/USDT:USDT | +20.20% | $2,403,917.67 |
| GRASS/USDT:USDT | +12.98% | $2,398,072.07 |
| NEAR/USDT:USDT | +11.42% | $148,040,429.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_relative_strength | +5.11% | +4.92% |
| NEAR/USDT:USDT | below_1h_threshold | +3.50% | +3.31% |
| CRO/USDT:USDT | below_1h_threshold | +2.64% | +2.45% |
| GRASS/USDT:USDT | below_1h_threshold | +2.62% | +2.42% |
| RAY/USDT:USDT | below_1h_threshold | +2.38% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
