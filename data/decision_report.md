# Decision Report

- generated_at: 2026-06-18T21:34:08.664170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7079**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=7079, expectancy=-0.05%
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
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.48% | **+0.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.12% | **+0.11%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.51** / 初期 $100.00 (+3.51%)
- 確定トレード: 17件 (TP 8 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.32** / 初期 $100.00 (+123.32%)
- 確定: 1899件 (Win 540 / Loss 607 / Flat 752) / skip 1741件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $223.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 182件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T21:34:04.361396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=62948.7
- Funnel: target 795 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +23.59% | $2,418,922.58 |
| EDEN/USDT:USDT | +18.03% | $1,616,382.79 |
| BASED/USDT:USDT | +17.78% | $2,234,618.75 |
| SYN/USDT:USDT | +16.53% | $18,419,981.21 |
| EIGEN/USDT:USDT | +11.23% | $2,535,309.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +4.60% | +4.78% |
| LAB/USDT:USDT | below_1h_threshold | +3.09% | +3.27% |
| JTO/USDT:USDT | below_1h_threshold | +3.04% | +3.22% |
| TAC/USDT:USDT | below_1h_threshold | +2.16% | +2.34% |
| BLESS/USDT:USDT | below_1h_threshold | +1.74% | +1.92% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
