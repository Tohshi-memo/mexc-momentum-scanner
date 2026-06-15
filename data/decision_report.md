# Decision Report

- generated_at: 2026-06-15T22:35:07.520208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6817**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=6817, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 9/20 | 45.0% | +2.90% | **+1.31%** |
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.63% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.62% | **+1.38%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.69% | **+1.18%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.47% | **+0.88%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.90% | **+0.86%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.97% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$181.52** / 初期 $100.00 (+81.52%)
- 確定: 1690件 (Win 443 / Loss 528 / Flat 719) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $181.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 73件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T22:35:03.444973+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=66223.3
- Funnel: target 772 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +30.91% | $2,472,960.50 |
| EVAA/USDT:USDT | +16.90% | $42,181,059.03 |
| HOME/USDT:USDT | +14.88% | $1,111,770.86 |
| SPCXSTOCK/USDT:USDT | +12.89% | $264,819,928.48 |
| FOLKS/USDT:USDT | +9.40% | $2,306,352.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +1.66% | +1.83% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.42% | +1.59% |
| ALLO/USDT:USDT | below_1h_threshold | +1.21% | +1.39% |
| HOME/USDT:USDT | below_1h_threshold | +1.01% | +1.19% |
| BABY/USDT:USDT | below_1h_threshold | +0.80% | +0.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
