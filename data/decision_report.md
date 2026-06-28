# Decision Report

- generated_at: 2026-06-28T03:21:56.726505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7727**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7727, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 3/16 | 18.8% | -0.00% | **-0.00%** |
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |
| ASK | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$241.92** / 初期 $100.00 (+141.92%)
- 確定: 2235件 (Win 674 / Loss 746 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $241.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 683件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T03:21:53.437610+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=60236.3
- Funnel: target 806 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWR/USDT:USDT | +18.64% | $1,337,033.25 |
| LAB/USDT:USDT | +15.85% | $40,383,977.88 |
| S/USDT:USDT | +12.56% | $4,818,899.95 |
| BASED/USDT:USDT | +9.37% | $1,283,626.67 |
| SIREN/USDT:USDT | +8.95% | $1,217,931.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +2.89% | +2.70% |
| ALLO/USDT:USDT | below_1h_threshold | +2.57% | +2.38% |
| S/USDT:USDT | below_1h_threshold | +2.53% | +2.34% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.70% | +1.51% |
| POWR/USDT:USDT | below_1h_threshold | +1.58% | +1.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
