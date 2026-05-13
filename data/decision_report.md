# Decision Report

- generated_at: 2026-05-13T08:13:02.585555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4200**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4200, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.87% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.91% | **+0.50%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.44% | **+0.28%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定: 336件 (Win 94 / Loss 119 / Flat 123) / skip 425件
- 成長率目線: 平均log +0.000561 / 幾何平均 +0.056% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUTH/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $120.75

## 4. Latest Market Context

- 更新: 2026-05-13T08:12:59.218484+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80935.1
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +44.29% | $1,339,188.18 |
| SATO/USDT:USDT | +23.13% | $1,284,426.19 |
| IRYS/USDT:USDT | +22.40% | $6,323,984.50 |
| INJ/USDT:USDT | +18.40% | $64,855,791.63 |
| LAB/USDT:USDT | +18.34% | $104,055,852.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +2.95% | +3.01% |
| UB/USDT:USDT | below_1h_threshold | +2.90% | +2.96% |
| COS/USDT:USDT | below_1h_threshold | +2.67% | +2.72% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.30% | +2.35% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.76% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
