# Decision Report

- generated_at: 2026-05-25T06:19:13.993953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4845**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=4845, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.09% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.67% | **+0.54%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.76% | **+0.53%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.64% | **+0.33%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.25** / 初期 $100.00 (+25.25%)
- 確定: 651件 (Win 163 / Loss 206 / Flat 282) / skip 755件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.82% 残高後 $125.25

## 4. Latest Market Context

- 更新: 2026-05-25T06:19:11.869410+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77278.1
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +34.67% | $3,504,695.15 |
| SPORTFUN/USDT:USDT | +15.67% | $1,263,093.96 |
| H/USDT:USDT | +8.50% | $1,194,423.74 |
| NIL/USDT:USDT | +7.83% | $14,551,808.78 |
| SAGA/USDT:USDT | +7.34% | $1,276,858.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +1.59% | +1.71% |
| GRASS/USDT:USDT | below_1h_threshold | +1.34% | +1.46% |
| INJ/USDT:USDT | below_1h_threshold | +1.00% | +1.12% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +0.95% | +1.06% |
| H/USDT:USDT | below_1h_threshold | +0.46% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
