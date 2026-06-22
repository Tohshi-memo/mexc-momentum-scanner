# Decision Report

- generated_at: 2026-06-22T16:54:03.095426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7381**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.37% / filled 20/20。**
- 全期間 MARKET基準: n=7381, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.44% | **+2.44%** |
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.67% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.26% | **+0.05%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.34% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.74** / 初期 $100.00 (+131.74%)
- 確定: 2037件 (Win 602 / Loss 670 / Flat 765) / skip 1905件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $231.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 480件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T16:53:57.801773+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64687.1
- Funnel: target 808 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1, 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +8.65% | $24,866,183.04 |
| BLESS/USDT:USDT | +6.43% | $3,301,563.62 |
| VELVET/USDT:USDT | +5.08% | $10,063,562.33 |
| RE/USDT:USDT | +4.22% | $22,724,547.71 |
| RESOLV/USDT:USDT | +3.92% | $12,901,359.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +4.22% | +4.41% |
| RESOLV/USDT:USDT | below_1h_threshold | +3.92% | +4.11% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.53% | +3.72% |
| AMCSTOCK/USDT:USDT | below_1h_threshold | +3.10% | +3.29% |
| POWER/USDT:USDT | below_1h_threshold | +2.91% | +3.10% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
