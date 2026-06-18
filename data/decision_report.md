# Decision Report

- generated_at: 2026-06-18T03:49:24.644683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7000**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7000, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.36% | **+0.11%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.16% | **-0.06%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.42% | **-0.11%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_8PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.63% | **+2.63%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.80% | **+1.17%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$214.06** / 初期 $100.00 (+114.06%)
- 確定: 1846件 (Win 513 / Loss 582 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $214.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.32** / 初期 $100.00 (+5.32%)
- 確定: 273件 (Win 75 / Loss 70 / Flat 128) / skip 138件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0614 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.32

## 5. Latest Market Context

- 更新: 2026-06-18T03:49:17.321710+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.54% price=64303.5
- Funnel: target 790 → liquid 173 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1, 4h RSI 78.5 >= 65=1, 4h RSI 72.0 >= 65=1, 4h RSI 66.9 >= 65=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +130.03% | $33,379,480.39 |
| O/USDT:USDT | +63.00% | $1,897,530.85 |
| SYN/USDT:USDT | +52.84% | $4,543,952.51 |
| HOME/USDT:USDT | +39.57% | $1,130,119.30 |
| H/USDT:USDT | +27.79% | $37,547,073.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.66% | +5.20% |
| EVAA/USDT:USDT | below_1h_threshold | +3.96% | +4.50% |
| H/USDT:USDT | below_1h_threshold | +3.39% | +3.93% |
| STG/USDT:USDT | below_1h_threshold | +2.96% | +3.50% |
| TAC/USDT:USDT | below_1h_threshold | +2.17% | +2.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
