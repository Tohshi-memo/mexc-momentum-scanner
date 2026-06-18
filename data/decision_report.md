# Decision Report

- generated_at: 2026-06-18T17:36:09.353920+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7066**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.82% / filled 20/20。**
- 全期間 MARKET基準: n=7066, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |
| ASK | 20/20 | 100.0% | +2.25% | **+2.25%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.53% | **+2.15%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.51% | **+2.01%** |
| LIMIT_BB3S | 6/19 | 31.6% | +4.92% | **+1.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.59% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$216.76** / 初期 $100.00 (+116.76%)
- 確定: 1887件 (Win 532 / Loss 604 / Flat 751) / skip 1740件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $216.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 169件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T17:36:00.696681+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62643.6
- Funnel: target 795 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +16.67% | $24,321,020.02 |
| ESPORTS/USDT:USDT | +9.88% | $51,523,181.13 |
| FOLKS/USDT:USDT | +9.22% | $5,921,401.00 |
| MYX/USDT:USDT | +6.12% | $3,536,475.66 |
| COAI/USDT:USDT | +4.81% | $1,483,384.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMCSTOCK/USDT:USDT | below_1h_threshold | +4.70% | +4.74% |
| HEI/USDT:USDT | below_1h_threshold | +2.54% | +2.57% |
| SATSSTOCK/USDT:USDT | below_1h_threshold | +2.27% | +2.31% |
| LAB/USDT:USDT | below_1h_threshold | +1.13% | +1.16% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.02% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
