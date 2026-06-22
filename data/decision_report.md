# Decision Report

- generated_at: 2026-06-22T13:47:11.961939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7370**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=7370, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.84% | **+1.84%** |
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_BB3S | 5/18 | 27.8% | +2.77% | **+0.77%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.42% | **+0.28%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.17% | **+0.17%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.11% | **+0.04%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.56% | **-0.39%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.57% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.97** / 初期 $100.00 (+2.97%)
- 確定トレード: 27件 (TP 11 / SL 16 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.97
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.45** / 初期 $100.00 (+129.45%)
- 確定: 2033件 (Win 599 / Loss 669 / Flat 765) / skip 1898件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $229.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 469件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T13:47:07.039139+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.51% price=65449.9
- Funnel: target 808 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +55.48% | $19,202,236.35 |
| BEL/USDT:USDT | +37.19% | $2,133,145.12 |
| BTW/USDT:USDT | +26.57% | $37,840,653.94 |
| CLO/USDT:USDT | +18.32% | $3,381,212.57 |
| LAYER/USDT:USDT | +17.78% | $3,600,366.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.87% | +4.36% |
| BTW/USDT:USDT | below_1h_threshold | +4.86% | +4.35% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +2.75% | +2.24% |
| SPX/USDT:USDT | below_1h_threshold | +2.44% | +1.93% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.95% | +1.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
