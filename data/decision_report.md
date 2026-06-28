# Decision Report

- generated_at: 2026-06-28T14:06:03.650245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7757**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7757, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +6.29% | **+1.26%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.41% | **+0.64%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.97% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$254.17** / 初期 $100.00 (+154.17%)
- 確定: 2265件 (Win 691 / Loss 759 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $254.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 713件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T14:05:58.939832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=60015.4
- Funnel: target 805 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACT/USDT:USDT | +77.90% | $8,902,883.05 |
| VELVET/USDT:USDT | +24.80% | $228,368,269.83 |
| S/USDT:USDT | +20.98% | $8,928,550.14 |
| SIREN/USDT:USDT | +17.42% | $1,919,587.84 |
| RAVE/USDT:USDT | +16.53% | $10,333,904.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACT/USDT:USDT | below_1h_threshold | +4.53% | +4.58% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.34% | +1.39% |
| VELVET/USDT:USDT | below_1h_threshold | +1.29% | +1.34% |
| SNX/USDT:USDT | below_1h_threshold | +0.95% | +1.00% |
| UB/USDT:USDT | below_1h_threshold | +0.61% | +0.66% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
