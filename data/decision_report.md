# Decision Report

- generated_at: 2026-07-06T00:50:17.080805+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8361**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8361, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +1.36% | **+0.27%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.68% | **+0.59%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.21% | **+0.54%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -0.00% | **-0.00%** |
| ASK_LONG | 20/20 | 100.0% | -0.04% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 65件 (TP 22 / SL 42 / EXP 1)
- 最新: MAGMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.33** / 初期 $100.00 (+220.33%)
- 確定: 2621件 (Win 832 / Loss 885 / Flat 904) / skip 2301件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEROC0MPUTE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $320.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1133件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T00:50:08.027503+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63671.2
- Funnel: target 835 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.2 >= 65=1, 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEROC0MPUTE/USDT:USDT | +25.64% | $1,608,906.61 |
| 4/USDT:USDT | +24.97% | $1,334,703.16 |
| TRB/USDT:USDT | +16.90% | $6,681,200.36 |
| GIGGLE/USDT:USDT | +16.47% | $1,416,872.70 |
| TLM/USDT:USDT | +9.87% | $42,713,810.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +4.94% | +4.85% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.88% | +2.80% |
| MIRA/USDT:USDT | below_1h_threshold | +2.77% | +2.69% |
| ARX/USDT:USDT | below_1h_threshold | +2.43% | +2.34% |
| EWY/USDT:USDT | below_1h_threshold | +2.35% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
