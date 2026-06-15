# Decision Report

- generated_at: 2026-06-15T17:19:15.219978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6799**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=6799, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.47% | **+0.30%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.80% | **+0.56%** |
| ASK_LONG | 20/20 | 100.0% | -0.07% | **-0.07%** |
| MARKET_LONG | 20/20 | 100.0% | -0.09% | **-0.09%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.15% | **-0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$175.50** / 初期 $100.00 (+75.50%)
- 確定: 1672件 (Win 435 / Loss 521 / Flat 716) / skip 1688件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account -0.34% 残高後 $175.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 55件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T17:19:11.085980+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=66881.7
- Funnel: target 772 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +10.56% | $41,663,863.54 |
| UAI/USDT:USDT | +5.29% | $4,272,963.26 |
| ASTEROID/USDT:USDT | +4.82% | $6,095,286.48 |
| XLM/USDT:USDT | +3.50% | $65,127,793.93 |
| SPCXSTOCK/USDT:USDT | +3.23% | $142,272,681.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +2.78% | +3.14% |
| BEAT/USDT:USDT | below_1h_threshold | +2.68% | +3.04% |
| SIREN/USDT:USDT | below_1h_threshold | +2.17% | +2.52% |
| OPG/USDT:USDT | below_1h_threshold | +1.98% | +2.33% |
| COAI/USDT:USDT | below_1h_threshold | +1.85% | +2.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
