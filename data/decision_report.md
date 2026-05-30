# Decision Report

- generated_at: 2026-05-30T17:29:43.058795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5142**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=5142, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.82% | **+1.37%** |
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_BB3S | 5/19 | 26.3% | +3.95% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.98% | **+0.24%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.05% | **+0.02%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.05% | **-0.03%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.13% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.59** / 初期 $100.00 (-1.41%)
- 確定トレード: 77件 (TP 23 / SL 51 / EXP 3)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.59
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 791件 (Win 183 / Loss 242 / Flat 366) / skip 912件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-30T17:29:40.428667+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73915.6
- Funnel: target 773 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +7.92% | $158,354,386.43 |
| H/USDT:USDT | +5.07% | $9,772,029.33 |
| STG/USDT:USDT | +3.62% | $2,930,690.75 |
| ALGO/USDT:USDT | +3.18% | $9,532,495.34 |
| CAKE/USDT:USDT | +3.11% | $1,116,675.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +2.16% | +2.14% |
| BASED/USDT:USDT | below_1h_threshold | +1.94% | +1.92% |
| LIT/USDT:USDT | below_1h_threshold | +1.91% | +1.89% |
| ASTER/USDT:USDT | below_1h_threshold | +1.70% | +1.68% |
| ALGO/USDT:USDT | below_1h_threshold | +1.68% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
