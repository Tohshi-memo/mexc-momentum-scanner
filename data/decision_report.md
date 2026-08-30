# Decision Report

- generated_at: 2026-08-30T15:06:20.744044+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13070**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=13070, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.43% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.47% | **+0.73%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.99% | **+0.45%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.12% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$774.83** / 初期 $100.00 (+674.83%)
- 確定: 4808件 (Win 1464 / Loss 1584 / Flat 1760) / skip 4823件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.01% 残高後 $774.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.79** / 初期 $100.00 (+71.79%)
- 確定: 2146件 (Win 593 / Loss 519 / Flat 1034) / skip 4335件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $171.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2083件 (Win 610 / Loss 812 / Flat 661) / pending 0件 / skip 2456件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-30T15:06:09.693829+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78662.4
- Funnel: target 1026 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +147.35% | $10,560,515.14 |
| HNT/USDT:USDT | +125.55% | $50,600,935.53 |
| ZKC/USDT:USDT | +65.82% | $6,450,286.49 |
| SKR/USDT:USDT | +60.07% | $5,260,521.72 |
| FONE/USDT:USDT | +48.12% | $1,415,491.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +3.38% | +3.49% |
| ZKP/USDT:USDT | below_1h_threshold | +2.18% | +2.29% |
| HNT/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| FONE/USDT:USDT | below_1h_threshold | +1.28% | +1.38% |
| UAI/USDT:USDT | below_1h_threshold | +1.22% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
