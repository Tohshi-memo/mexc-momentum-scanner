# Decision Report

- generated_at: 2026-05-30T17:14:48.020850+00:00
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

- 更新: 2026-05-30T17:14:45.820936+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73869.9
- Funnel: target 773 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +8.29% | $4,962,477.35 |
| H/USDT:USDT | +4.92% | $9,540,143.94 |
| LAB/USDT:USDT | +4.03% | $153,868,016.78 |
| CAKE/USDT:USDT | +3.82% | $1,037,129.60 |
| TONCOIN/USDT:USDT | +2.52% | $34,775,518.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.94% | +3.98% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.63% | +2.67% |
| LIT/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |
| ASTER/USDT:USDT | below_1h_threshold | +0.68% | +0.72% |
| ZRO/USDT:USDT | below_1h_threshold | +0.62% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
