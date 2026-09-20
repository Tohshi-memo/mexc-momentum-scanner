# Decision Report

- generated_at: 2026-09-20T17:51:32.821325+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15200**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.98% / filled 20/20。**
- 全期間 MARKET基準: n=15200, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.12% | **+0.90%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.89% | **+0.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.60% | **+0.54%** |
| LIMIT_BB3S | 9/14 | 64.3% | +0.76% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +6.37% | **+1.27%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.29% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6044件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3293件 (Win 911 / Loss 764 / Flat 1618) / skip 5318件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定: 2989件 (Win 882 / Loss 1180 / Flat 927) / pending 5件 / skip 3685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.62

## 6. Latest Market Context

- 更新: 2026-09-20T17:51:20.599945+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81284.5
- Funnel: target 1050 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1, 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AR/USDT:USDT | +18.84% | $7,179,720.80 |
| LUNANEW/USDT:USDT | +15.22% | $1,723,493.90 |
| ENA/USDT:USDT | +11.30% | $73,384,986.69 |
| AKE/USDT:USDT | +9.88% | $86,942,005.61 |
| SAGA/USDT:USDT | +8.34% | $4,206,005.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.50% | +3.51% |
| ZAMA/USDT:USDT | below_1h_threshold | +3.35% | +3.37% |
| STRK/USDT:USDT | below_1h_threshold | +2.57% | +2.58% |
| OP/USDT:USDT | below_1h_threshold | +2.27% | +2.28% |
| BTW/USDT:USDT | below_1h_threshold | +1.66% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
