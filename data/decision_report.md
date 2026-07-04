# Decision Report

- generated_at: 2026-07-04T21:58:52.758569+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8295**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8295, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.71% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.70% | **+0.35%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.39% | **+0.18%** |
| ASK_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.07% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.78** / 初期 $100.00 (+231.78%)
- 確定: 2612件 (Win 831 / Loss 877 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $331.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1069件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0018 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T21:58:47.786166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63301.1
- Funnel: target 834 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +22.28% | $3,666,986.69 |
| RPL/USDT:USDT | +20.25% | $2,551,193.99 |
| H/USDT:USDT | +13.43% | $3,108,971.90 |
| HMSTR/USDT:USDT | +12.62% | $16,715,920.91 |
| HOT/USDT:USDT | +11.81% | $1,274,248.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_relative_strength | +5.12% | +4.97% |
| HMSTR/USDT:USDT | below_1h_threshold | +4.01% | +3.87% |
| O/USDT:USDT | below_1h_threshold | +4.01% | +3.87% |
| H/USDT:USDT | below_1h_threshold | +2.88% | +2.73% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.42% | +2.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
