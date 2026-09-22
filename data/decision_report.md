# Decision Report

- generated_at: 2026-09-22T04:21:20.242539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15294**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.87% / filled 20/20。**
- 全期間 MARKET基準: n=15294, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.87% | **+1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.51% | **+2.26%** |
| MARKET | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_BB3S | 6/18 | 33.3% | +3.33% | **+1.11%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.85% | **+0.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.86% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.10% | **+0.05%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,177.42** / 初期 $100.00 (+1077.42%)
- 確定: 5785件 (Win 1721 / Loss 1862 / Flat 2202) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,177.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.71** / 初期 $100.00 (+148.71%)
- 確定: 3333件 (Win 921 / Loss 773 / Flat 1639) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $248.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 3066件 (Win 902 / Loss 1200 / Flat 964) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.76

## 6. Latest Market Context

- 更新: 2026-09-22T04:21:09.206924+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=85467.1
- Funnel: target 1057 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +35.71% | $3,053,437.16 |
| ALCH/USDT:USDT | +17.57% | $2,473,679.14 |
| GRASS/USDT:USDT | +12.98% | $2,527,587.43 |
| FORM/USDT:USDT | +12.77% | $9,544,875.41 |
| CRO/USDT:USDT | +8.37% | $1,337,914.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.04% | +4.26% |
| DOGE/USDT:USDT | below_1h_threshold | +2.94% | +3.17% |
| SHIB/USDT:USDT | below_1h_threshold | +2.44% | +2.67% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.62% | +1.84% |
| MINA/USDT:USDT | below_1h_threshold | +1.56% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
