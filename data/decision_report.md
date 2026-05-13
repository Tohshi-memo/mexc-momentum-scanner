# Decision Report

- generated_at: 2026-05-13T08:53:24.107136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4203**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4203, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.91% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.17% | **+0.13%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.03** / 初期 $100.00 (+20.03%)
- 確定: 339件 (Win 94 / Loss 122 / Flat 123) / skip 425件
- 成長率目線: 平均log +0.000539 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $120.03

## 4. Latest Market Context

- 更新: 2026-05-13T08:53:10.878636+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81153.1
- Funnel: target 764 → liquid 189 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1, 4h RSI 78.6 >= 65=1, 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +43.32% | $1,512,827.75 |
| LAB/USDT:USDT | +29.69% | $108,577,141.46 |
| IRYS/USDT:USDT | +22.61% | $6,667,362.38 |
| UB/USDT:USDT | +22.40% | $4,884,706.03 |
| SATO/USDT:USDT | +20.19% | $1,309,735.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +3.06% | +2.85% |
| BASED/USDT:USDT | below_1h_threshold | +3.00% | +2.79% |
| KITE/USDT:USDT | below_1h_threshold | +2.80% | +2.58% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.15% | +1.94% |
| TURBO/USDT:USDT | below_1h_threshold | +2.06% | +1.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
