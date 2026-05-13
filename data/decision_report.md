# Decision Report

- generated_at: 2026-05-13T04:03:21.159777+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4184**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=4184, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.88% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.58% | **+1.10%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.51% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.01% | **+0.00%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.22** / 初期 $100.00 (+19.22%)
- 確定: 320件 (Win 91 / Loss 114 / Flat 115) / skip 425件
- 成長率目線: 平均log +0.000549 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $119.22

## 4. Latest Market Context

- 更新: 2026-05-13T04:03:18.073668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81188.0
- Funnel: target 762 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +32.70% | $3,402,995.10 |
| LAB/USDT:USDT | +17.75% | $103,417,316.53 |
| PEAQ/USDT:USDT | +17.03% | $2,432,281.16 |
| SATO/USDT:USDT | +16.70% | $1,059,016.90 |
| TIA/USDT:USDT | +14.60% | $29,586,075.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.45% | +2.48% |
| SATO/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.56% | +1.59% |
| STRK/USDT:USDT | below_1h_threshold | +0.60% | +0.63% |
| LAB/USDT:USDT | below_1h_threshold | +0.53% | +0.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
