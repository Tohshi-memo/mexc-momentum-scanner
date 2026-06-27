# Decision Report

- generated_at: 2026-06-27T16:56:47.973568+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7705**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7705, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +5.45% | **+0.82%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.83% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.63% | **+0.17%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.52** / 初期 $100.00 (+132.52%)
- 確定: 2216件 (Win 662 / Loss 739 / Flat 815) / skip 2050件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $232.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定: 436件 (Win 117 / Loss 111 / Flat 208) / skip 680件
- 成長率目線: 平均log +0.000165 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0379 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.44

## 5. Latest Market Context

- 更新: 2026-06-27T16:56:37.579595+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=60786.1
- Funnel: target 806 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +6.42% | $1,932,563.09 |
| ALLO/USDT:USDT | +6.01% | $15,234,591.57 |
| LAB/USDT:USDT | +5.38% | $39,572,568.28 |
| PIEVERSE/USDT:USDT | +3.21% | $1,166,088.35 |
| PUMPFUN/USDT:USDT | +2.44% | $5,667,055.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.14% | +3.19% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.45% | +2.50% |
| WIF/USDT:USDT | below_1h_threshold | +2.13% | +2.18% |
| UNI/USDT:USDT | below_1h_threshold | +1.60% | +1.65% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.56% | +1.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
