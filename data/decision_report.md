# Decision Report

- generated_at: 2026-06-28T13:57:33.961953+00:00
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

- 更新: 2026-06-28T13:57:25.796250+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=60053.6
- Funnel: target 805 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACT/USDT:USDT | +73.03% | $8,643,006.60 |
| VELVET/USDT:USDT | +23.93% | $245,306,545.22 |
| S/USDT:USDT | +22.34% | $8,865,911.08 |
| RAVE/USDT:USDT | +18.60% | $10,349,396.03 |
| SIREN/USDT:USDT | +17.82% | $1,925,159.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.70% | +4.06% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.39% | +3.75% |
| SIREN/USDT:USDT | below_1h_threshold | +2.06% | +2.42% |
| BILL/USDT:USDT | below_1h_threshold | +1.59% | +1.95% |
| S/USDT:USDT | below_1h_threshold | +1.29% | +1.65% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
