# Decision Report

- generated_at: 2026-05-30T23:54:49.021399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5152**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=5152, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.34% | **+1.20%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.57% | **+0.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.41% | **+0.39%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.15% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 78件 (TP 23 / SL 52 / EXP 3)
- 最新: NFP/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 791件 (Win 183 / Loss 242 / Flat 366) / skip 922件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-30T23:54:46.808304+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=73810.0
- Funnel: target 773 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TA/USDT:USDT | +19.40% | $1,992,325.21 |
| BIANRENSHENG/USDT:USDT | +16.62% | $1,253,494.88 |
| ONDO/USDT:USDT | +9.45% | $32,251,064.49 |
| MYX/USDT:USDT | +7.31% | $1,865,173.74 |
| STG/USDT:USDT | +7.30% | $3,358,275.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +4.72% | +4.77% |
| MYX/USDT:USDT | below_1h_threshold | +2.34% | +2.39% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.31% | +2.37% |
| RIVER/USDT:USDT | below_1h_threshold | +1.55% | +1.60% |
| LAB/USDT:USDT | below_1h_threshold | +1.55% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
