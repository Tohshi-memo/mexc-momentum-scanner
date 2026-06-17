# Decision Report

- generated_at: 2026-06-17T06:24:48.228240+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6911, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.54% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK_LONG | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.89% | **+2.02%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.83** / 初期 $100.00 (+97.83%)
- 確定: 1784件 (Win 482 / Loss 557 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.19** / 初期 $100.00 (+1.19%)
- 確定: 184件 (Win 41 / Loss 35 / Flat 108) / skip 138件
- 成長率目線: 平均log +0.000064 / 幾何平均 +0.006% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $101.19

## 5. Latest Market Context

- 更新: 2026-06-17T06:24:43.845371+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=65802.9
- Funnel: target 785 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +28.73% | $4,141,142.02 |
| SQD/USDT:USDT | +27.37% | $1,814,739.82 |
| SPX/USDT:USDT | +26.11% | $7,389,061.10 |
| ROAM/USDT:USDT | +22.25% | $3,609,804.22 |
| UNI/USDT:USDT | +20.48% | $46,329,829.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.98% | +4.97% |
| UNI/USDT:USDT | below_1h_threshold | +3.80% | +3.79% |
| SPX/USDT:USDT | below_1h_threshold | +2.40% | +2.39% |
| TRIA/USDT:USDT | below_1h_threshold | +2.15% | +2.14% |
| LDO/USDT:USDT | below_1h_threshold | +1.85% | +1.84% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
