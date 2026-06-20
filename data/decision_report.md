# Decision Report

- generated_at: 2026-06-20T16:37:59.991108+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7250**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=7250, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.55% | **+2.04%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.62% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.22% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.21% | **+0.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.08% | **+0.04%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.03% | **+0.01%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.50% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.07** / 初期 $100.00 (+127.07%)
- 確定: 1979件 (Win 576 / Loss 645 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 351件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T16:37:52.542436+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=63880.8
- Funnel: target 796 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +7.66% | $12,804,738.15 |
| LAB/USDT:USDT | +4.77% | $29,745,834.50 |
| BICO/USDT:USDT | +4.58% | $33,603,306.33 |
| ASTEROID/USDT:USDT | +4.12% | $1,951,738.76 |
| SYN/USDT:USDT | +3.50% | $7,945,588.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.72% | +5.11% |
| BICO/USDT:USDT | below_1h_threshold | +4.59% | +4.98% |
| ASTEROID/USDT:USDT | below_1h_threshold | +4.12% | +4.51% |
| SYN/USDT:USDT | below_1h_threshold | +3.51% | +3.90% |
| BLESS/USDT:USDT | below_1h_threshold | +2.87% | +3.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
