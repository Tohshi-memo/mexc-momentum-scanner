# Decision Report

- generated_at: 2026-05-27T14:59:26.528829+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4929**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=4929, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.49% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.66% | **+0.36%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.07%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.07% | **+0.06%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.74% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 806件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T14:59:24.050024+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=75013.7
- Funnel: target 775 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +16.68% | $26,434,034.52 |
| RIF/USDT:USDT | +15.87% | $1,754,423.54 |
| LUNC/USDT:USDT | +14.77% | $16,012,913.93 |
| ESPORTS/USDT:USDT | +10.57% | $9,104,632.88 |
| ALT/USDT:USDT | +10.29% | $2,949,285.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.17% |
| LUNC/USDT:USDT | below_1h_threshold | +2.89% | +2.94% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.10% | +2.15% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +1.71% | +1.76% |
| CHZ/USDT:USDT | below_1h_threshold | +1.26% | +1.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
