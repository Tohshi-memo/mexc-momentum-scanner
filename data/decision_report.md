# Decision Report

- generated_at: 2026-06-18T21:54:38.838591+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7082**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=7082, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.86% | **+0.39%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.12% | **+0.11%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.85% | **+0.59%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.51** / 初期 $100.00 (+3.51%)
- 確定トレード: 17件 (TP 8 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.31** / 初期 $100.00 (+123.31%)
- 確定: 1902件 (Win 541 / Loss 609 / Flat 752) / skip 1741件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $223.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 185件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T21:54:33.458431+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62866.3
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +133.21% | $1,662,096.98 |
| ZEREBRO/USDT:USDT | +25.03% | $2,508,729.79 |
| EDEN/USDT:USDT | +16.06% | $1,746,676.25 |
| BASED/USDT:USDT | +15.56% | $2,293,099.77 |
| SYN/USDT:USDT | +15.25% | $18,678,305.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +2.87% | +3.18% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.88% | +2.20% |
| JTO/USDT:USDT | below_1h_threshold | +1.79% | +2.10% |
| LAB/USDT:USDT | below_1h_threshold | +1.79% | +2.10% |
| TAC/USDT:USDT | below_1h_threshold | +1.23% | +1.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
