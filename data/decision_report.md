# Decision Report

- generated_at: 2026-06-14T19:55:46.815133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6696**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6696, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.96% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.42% | **+0.19%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.58** / 初期 $100.00 (+71.58%)
- 確定: 1569件 (Win 417 / Loss 498 / Flat 654) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $171.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.57** / 初期 $100.00 (-1.43%)
- 確定: 72件 (Win 19 / Loss 15 / Flat 38) / skip 35件
- 成長率目線: 平均log -0.000200 / 幾何平均 -0.020% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $98.57

## 5. Latest Market Context

- 更新: 2026-06-14T19:55:41.290444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63756.9
- Funnel: target 770 → liquid 130 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +29.88% | $7,752,619.98 |
| BABY/USDT:USDT | +8.30% | $1,475,443.67 |
| H/USDT:USDT | +7.97% | $122,395,070.70 |
| BP/USDT:USDT | +7.44% | $1,029,060.39 |
| BANANAS31/USDT:USDT | +6.65% | $2,399,966.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +3.09% | +3.13% |
| OPG/USDT:USDT | below_1h_threshold | +2.94% | +2.98% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +2.51% | +2.56% |
| MEGA/USDT:USDT | below_1h_threshold | +1.48% | +1.53% |
| RAVE/USDT:USDT | below_1h_threshold | +1.48% | +1.52% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
