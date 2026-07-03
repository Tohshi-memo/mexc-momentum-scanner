# Decision Report

- generated_at: 2026-07-03T16:36:06.463587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.68% / filled 20/20。**
- 全期間 MARKET基準: n=8174, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |
| ASK | 20/20 | 100.0% | +2.04% | **+2.04%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.73% | **+1.30%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.68% | **+0.41%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.65% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.13% | **+0.09%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.52% | **-0.29%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.79% | **-0.36%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 56件 (TP 20 / SL 35 / EXP 1)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.09** / 初期 $100.00 (+184.09%)
- 確定: 2493件 (Win 766 / Loss 833 / Flat 894) / skip 2242件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.08% 残高後 $284.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 974件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T16:35:58.976433+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62048.0
- Funnel: target 834 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +13.81% | $8,278,441.39 |
| GUA/USDT:USDT | +11.57% | $5,868,156.25 |
| XPL/USDT:USDT | +4.24% | $20,373,380.49 |
| BASED/USDT:USDT | +3.47% | $8,985,548.10 |
| ARPA/USDT:USDT | +2.92% | $7,072,434.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.29% | +4.05% |
| BASED/USDT:USDT | below_1h_threshold | +3.51% | +3.26% |
| ARPA/USDT:USDT | below_1h_threshold | +3.30% | +3.05% |
| TLM/USDT:USDT | below_1h_threshold | +2.68% | +2.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.59% | +2.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
