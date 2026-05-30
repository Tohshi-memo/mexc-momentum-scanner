# Decision Report

- generated_at: 2026-05-30T22:09:40.952694+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5149**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=5149, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.58% | **+1.58%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.98% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.24% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.29% | **+0.16%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.59** / 初期 $100.00 (-1.41%)
- 確定トレード: 77件 (TP 23 / SL 51 / EXP 3)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.59
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 791件 (Win 183 / Loss 242 / Flat 366) / skip 919件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-30T22:09:38.732543+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=73849.9
- Funnel: target 773 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TA/USDT:USDT | +19.40% | $1,891,422.99 |
| IO/USDT:USDT | +10.77% | $1,214,810.82 |
| ONDO/USDT:USDT | +7.70% | $27,448,944.54 |
| MYX/USDT:USDT | +6.58% | $1,587,746.37 |
| AVNT/USDT:USDT | +6.07% | $1,271,533.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +3.66% | +3.80% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.42% | +1.56% |
| MYX/USDT:USDT | below_1h_threshold | +0.30% | +0.44% |
| ID/USDT:USDT | below_1h_threshold | +0.23% | +0.37% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +0.16% | +0.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
