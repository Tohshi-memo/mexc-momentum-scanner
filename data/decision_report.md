# Decision Report

- generated_at: 2026-07-29T02:01:22.924884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9751**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.05% / filled 20/20。**
- 全期間 MARKET基準: n=9751, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+4.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.05% | **+4.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.05% | **+4.05%** |
| LIMIT_1PCT | 15/20 | 75.0% | +3.20% | **+2.40%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.59% | **+1.55%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.30% | **+1.27%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -1.64% | **-0.57%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -0.93% | **-0.60%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | -1.52% | **-1.37%** |

## 2. $100 Live Portfolio

- 残高: **$116.35** / 初期 $100.00 (+16.35%)
- 確定トレード: 158件 (TP 60 / SL 93 / EXP 5)
- 最新: DRAM/USDT:USDT TP_HIT PnL +7.69% 残高後 $116.35
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$496.53** / 初期 $100.00 (+396.53%)
- 確定: 3518件 (Win 1113 / Loss 1146 / Flat 1259) / skip 2794件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $496.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1936件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.55** / 初期 $100.00 (+10.55%)
- 確定: 758件 (Win 246 / Loss 289 / Flat 223) / pending 2件 / skip 466件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000242 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KAITO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $110.55

## 6. Latest Market Context

- 更新: 2026-07-29T02:01:16.819457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63656.0
- Funnel: target 904 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +17.95% | $1,227,211.01 |
| ON/USDT:USDT | +15.56% | $51,796,413.80 |
| BEAT/USDT:USDT | +13.65% | $45,127,166.88 |
| BTW/USDT:USDT | +13.30% | $6,129,324.99 |
| KAITO/USDT:USDT | +9.67% | $9,439,406.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.25% |
| LA/USDT:USDT | below_1h_threshold | +1.44% | +1.48% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.75% | +0.79% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.48% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
