# Decision Report

- generated_at: 2026-06-01T17:45:42.473657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5349**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5349, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.67% | **+1.51%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.21% | **+1.47%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.39% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 1016件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T17:45:40.227538+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=71688.7
- Funnel: target 773 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1, 4h RSI 65.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +33.33% | $2,452,472.30 |
| VIC/USDT:USDT | +15.72% | $1,875,518.98 |
| MERL/USDT:USDT | +8.35% | $1,753,602.23 |
| APE/USDT:USDT | +6.44% | $1,660,534.77 |
| JUP/USDT:USDT | +6.12% | $2,706,280.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APE/USDT:USDT | below_1h_threshold | +4.11% | +3.90% |
| OP/USDT:USDT | below_1h_threshold | +3.19% | +2.98% |
| NEAR/USDT:USDT | below_1h_threshold | +3.10% | +2.89% |
| CHZ/USDT:USDT | below_1h_threshold | +2.86% | +2.65% |
| JUP/USDT:USDT | below_1h_threshold | +2.68% | +2.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
