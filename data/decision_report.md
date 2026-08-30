# Decision Report

- generated_at: 2026-08-30T15:46:30.842522+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13076**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=13076, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.83% | **+0.17%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.11% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.85%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$770.96** / 初期 $100.00 (+670.96%)
- 確定: 4811件 (Win 1464 / Loss 1585 / Flat 1762) / skip 4826件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $770.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.79** / 初期 $100.00 (+71.79%)
- 確定: 2146件 (Win 593 / Loss 519 / Flat 1034) / skip 4341件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $171.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2083件 (Win 610 / Loss 812 / Flat 661) / pending 0件 / skip 2464件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-30T15:46:20.887814+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78815.0
- Funnel: target 1026 → liquid 117 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.7 >= 65=1, 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +161.17% | $11,817,988.43 |
| HNT/USDT:USDT | +159.64% | $57,106,605.72 |
| SKR/USDT:USDT | +62.25% | $5,521,087.14 |
| ZKC/USDT:USDT | +62.24% | $6,899,697.63 |
| PONS/USDT:USDT | +50.42% | $1,829,243.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_relative_strength | +5.04% | +4.96% |
| UAI/USDT:USDT | below_1h_threshold | +4.67% | +4.59% |
| PONS/USDT:USDT | below_1h_threshold | +2.51% | +2.42% |
| ZEC/USDT:USDT | below_1h_threshold | +1.85% | +1.76% |
| ZKP/USDT:USDT | below_1h_threshold | +1.28% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
