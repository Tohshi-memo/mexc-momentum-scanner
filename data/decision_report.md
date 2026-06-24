# Decision Report

- generated_at: 2026-06-24T01:30:43.735497+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7451**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=7451, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.47% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -2.04% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.21% | **+1.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.87% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 31件 (TP 12 / SL 19 / EXP 0)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.46** / 初期 $100.00 (+130.46%)
- 確定: 2082件 (Win 618 / Loss 690 / Flat 774) / skip 1930件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $230.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 534件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T01:30:36.558496+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62899.9
- Funnel: target 802 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +62.85% | $9,382,567.14 |
| BEAT/USDT:USDT | +23.31% | $63,592,857.57 |
| CLO/USDT:USDT | +14.81% | $5,385,348.58 |
| DYDX/USDT:USDT | +11.41% | $4,029,862.88 |
| ALLO/USDT:USDT | +8.80% | $5,200,814.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +1.76% | +1.89% |
| KAS/USDT:USDT | below_1h_threshold | +1.62% | +1.75% |
| BEAT/USDT:USDT | below_1h_threshold | +1.52% | +1.65% |
| UP/USDT:USDT | below_1h_threshold | +1.29% | +1.42% |
| DASH/USDT:USDT | below_1h_threshold | +1.10% | +1.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
