# Decision Report

- generated_at: 2026-06-14T04:52:12.703291+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6638**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6638, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.86% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.84** / 初期 $100.00 (+69.84%)
- 確定: 1511件 (Win 406 / Loss 483 / Flat 622) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $169.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 46件 (Win 16 / Loss 12 / Flat 18) / skip 3件
- 成長率目線: 平均log -0.000282 / 幾何平均 -0.028% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T04:52:06.651094+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=64328.1
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +62.41% | $25,007,099.52 |
| TRADOOR/USDT:USDT | +49.49% | $5,049,442.08 |
| BTW/USDT:USDT | +22.19% | $2,562,990.61 |
| BRETT/USDT:USDT | +10.97% | $1,559,285.75 |
| VELVET/USDT:USDT | +9.53% | $55,477,225.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +3.54% | +3.83% |
| H/USDT:USDT | below_1h_threshold | +3.31% | +3.60% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.26% | +2.55% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.73% | +2.02% |
| SIREN/USDT:USDT | below_1h_threshold | +1.54% | +1.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
