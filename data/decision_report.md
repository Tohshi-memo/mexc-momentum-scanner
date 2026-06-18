# Decision Report

- generated_at: 2026-06-18T17:12:57.790610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7063**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.82% / filled 20/20。**
- 全期間 MARKET基準: n=7063, expectancy=-0.05%
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
| ASK | 20/20 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.51% | **+2.01%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.19% | **+1.75%** |
| LIMIT_BB3S | 6/20 | 30.0% | +4.92% | **+1.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.72% | **+0.40%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.23% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$218.95** / 初期 $100.00 (+118.95%)
- 確定: 1885件 (Win 532 / Loss 602 / Flat 751) / skip 1739件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $218.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 166件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T17:12:46.994168+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=62400.3
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +32.46% | $21,179,934.74 |
| ESPORTS/USDT:USDT | +11.05% | $51,081,479.99 |
| FOLKS/USDT:USDT | +10.73% | $5,764,186.79 |
| PLAY/USDT:USDT | +6.56% | $1,516,774.46 |
| AIOT/USDT:USDT | +5.38% | $1,399,730.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.19% | +2.61% |
| HEI/USDT:USDT | below_1h_threshold | +1.73% | +2.15% |
| ALLO/USDT:USDT | below_1h_threshold | +0.99% | +1.41% |
| LAB/USDT:USDT | below_1h_threshold | +0.96% | +1.38% |
| MYX/USDT:USDT | below_1h_threshold | +0.77% | +1.19% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
