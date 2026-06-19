# Decision Report

- generated_at: 2026-06-19T02:36:00.356866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7094**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7094, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.48% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.33% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.26% | **+0.95%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.56% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.16** / 初期 $100.00 (+122.16%)
- 確定: 1914件 (Win 546 / Loss 615 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASED/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $222.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 197件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T02:35:55.144951+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62992.8
- Funnel: target 795 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +93.17% | $6,122,875.65 |
| BASED/USDT:USDT | +36.78% | $4,220,046.96 |
| ZEREBRO/USDT:USDT | +20.60% | $3,396,605.61 |
| EDEN/USDT:USDT | +17.69% | $2,203,293.81 |
| LAB/USDT:USDT | +14.83% | $35,753,339.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.33% | +4.33% |
| BASED/USDT:USDT | below_1h_threshold | +3.32% | +3.32% |
| EDEN/USDT:USDT | below_1h_threshold | +3.24% | +3.24% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.91% | +2.91% |
| LAB/USDT:USDT | below_1h_threshold | +2.62% | +2.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
