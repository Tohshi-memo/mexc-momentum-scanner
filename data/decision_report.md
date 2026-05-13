# Decision Report

- generated_at: 2026-05-13T04:13:12.587328+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4186**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=4186, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.65% | **+1.48%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.72% | **+1.20%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.70% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.28% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.01% | **+0.00%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.15** / 初期 $100.00 (+19.15%)
- 確定: 322件 (Win 91 / Loss 115 / Flat 116) / skip 425件
- 成長率目線: 平均log +0.000544 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $119.15

## 4. Latest Market Context

- 更新: 2026-05-13T04:13:08.817730+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81130.0
- Funnel: target 762 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +33.80% | $3,449,908.03 |
| SATO/USDT:USDT | +21.74% | $1,071,165.19 |
| PEAQ/USDT:USDT | +17.60% | $2,466,760.18 |
| LAB/USDT:USDT | +15.86% | $104,148,548.15 |
| TIA/USDT:USDT | +15.29% | $30,045,869.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.95% | +3.06% |
| VELO/USDT:USDT | below_1h_threshold | +1.65% | +1.76% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.31% | +1.42% |
| IRYS/USDT:USDT | below_1h_threshold | +1.22% | +1.32% |
| TIA/USDT:USDT | below_1h_threshold | +1.13% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
