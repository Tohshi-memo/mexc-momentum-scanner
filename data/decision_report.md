# Decision Report

- generated_at: 2026-05-30T14:54:39.836629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5132**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=5132, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.11% | **+1.05%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.60% | **+0.75%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.48% | **+1.39%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.39% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 76件 (TP 22 / SL 51 / EXP 3)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.00** / 初期 $100.00 (+24.00%)
- 確定: 787件 (Win 183 / Loss 240 / Flat 364) / skip 906件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +5.48%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $124.00

## 4. Latest Market Context

- 更新: 2026-05-30T14:54:37.574522+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=73900.0
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +59.03% | $3,977,068.89 |
| LAB/USDT:USDT | +38.34% | $146,625,526.56 |
| STG/USDT:USDT | +35.88% | $2,307,474.97 |
| H/USDT:USDT | +31.01% | $7,496,452.15 |
| NFP/USDT:USDT | +29.52% | $3,738,573.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.47% | +4.34% |
| FET/USDT:USDT | below_1h_threshold | +2.26% | +2.14% |
| WLD/USDT:USDT | below_1h_threshold | +2.01% | +1.88% |
| INJ/USDT:USDT | below_1h_threshold | +1.82% | +1.69% |
| H/USDT:USDT | below_1h_threshold | +1.64% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
