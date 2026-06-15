# Decision Report

- generated_at: 2026-06-15T15:17:17.681864+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6791**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6791, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.28% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.18% | **+0.12%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.17% | **+0.05%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$175.81** / 初期 $100.00 (+75.81%)
- 確定: 1664件 (Win 433 / Loss 516 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $175.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.16** / 初期 $100.00 (-1.84%)
- 確定: 152件 (Win 28 / Loss 28 / Flat 96) / skip 50件
- 成長率目線: 平均log -0.000122 / 幾何平均 -0.012% per trade / maxDD +2.48%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JTO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $98.16

## 5. Latest Market Context

- 更新: 2026-06-15T15:17:12.732811+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=66555.0
- Funnel: target 772 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +81.24% | $38,550,548.48 |
| ASTEROID/USDT:USDT | +71.15% | $5,853,925.88 |
| JTO/USDT:USDT | +44.65% | $4,600,002.79 |
| CLO/USDT:USDT | +40.81% | $2,217,876.08 |
| BSB/USDT:USDT | +39.49% | $10,292,315.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.02% | +3.01% |
| CLO/USDT:USDT | below_1h_threshold | +2.14% | +2.14% |
| XLM/USDT:USDT | below_1h_threshold | +1.71% | +1.70% |
| JTO/USDT:USDT | below_1h_threshold | +1.48% | +1.47% |
| XPL/USDT:USDT | below_1h_threshold | +1.46% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
