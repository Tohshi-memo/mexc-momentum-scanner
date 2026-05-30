# Decision Report

- generated_at: 2026-05-30T12:24:38.932607+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5124**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=5124, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.29% | **+1.95%** |
| ASK | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.86% | **+1.30%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.21% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.89% | **+0.45%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.11% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.75** / 初期 $100.00 (+24.75%)
- 確定: 779件 (Win 182 / Loss 237 / Flat 360) / skip 906件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +4.91%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $124.75

## 4. Latest Market Context

- 更新: 2026-05-30T12:24:36.384865+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=73632.7
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +35.37% | $2,020,161.12 |
| NFP/USDT:USDT | +33.50% | $3,283,720.01 |
| STG/USDT:USDT | +32.74% | $1,036,432.90 |
| LAB/USDT:USDT | +29.26% | $122,688,705.43 |
| VTHO/USDT:USDT | +20.54% | $1,734,819.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_relative_strength | +5.02% | +4.93% |
| PORTAL/USDT:USDT | below_1h_threshold | +3.88% | +3.80% |
| NFP/USDT:USDT | below_1h_threshold | +2.91% | +2.82% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.71% |
| FET/USDT:USDT | below_1h_threshold | +1.65% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
