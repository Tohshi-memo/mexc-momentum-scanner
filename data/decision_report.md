# Decision Report

- generated_at: 2026-08-16T04:46:19.556899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11716**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=11716, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.61% | **+1.53%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.05% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.85% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.49% | **+0.82%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.93% | **+0.42%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.67% | **+0.25%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.05% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.02** / 初期 $100.00 (+524.02%)
- 確定: 4182件 (Win 1292 / Loss 1362 / Flat 1528) / skip 4095件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $624.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.79** / 初期 $100.00 (+54.79%)
- 確定: 1769件 (Win 493 / Loss 416 / Flat 860) / skip 3358件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $154.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1560件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000108 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T04:46:11.011514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63090.8
- Funnel: target 986 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +27.46% | $5,750,337.81 |
| SPORTFUN/USDT:USDT | +17.33% | $4,301,961.59 |
| CROSS/USDT:USDT | +15.61% | $1,239,978.18 |
| BASED/USDT:USDT | +11.49% | $2,180,865.66 |
| CHIP/USDT:USDT | +10.22% | $1,933,662.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.77% | +3.78% |
| PRL/USDT:USDT | below_1h_threshold | +3.04% | +3.04% |
| US/USDT:USDT | below_1h_threshold | +2.65% | +2.66% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.57% | +2.57% |
| CHIP/USDT:USDT | below_1h_threshold | +1.70% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
