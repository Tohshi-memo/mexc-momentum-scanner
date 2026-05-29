# Decision Report

- generated_at: 2026-05-29T10:34:56.684537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5037**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=5037, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.50% | **+1.50%** |
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.27% | **+0.16%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.14% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.78% | **+0.74%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| ASK_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.38% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$99.09** / 初期 $100.00 (-0.91%)
- 確定トレード: 73件 (TP 22 / SL 48 / EXP 3)
- 最新: NIL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 858件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T10:34:53.726192+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=73590.0
- Funnel: target 777 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1, 4h RSI 97.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +171.76% | $86,667,689.57 |
| DELLSTOCK/USDT:USDT | +33.27% | $9,279,528.91 |
| IO/USDT:USDT | +22.45% | $3,678,938.97 |
| LAB/USDT:USDT | +19.62% | $63,894,754.13 |
| CTR/USDT:USDT | +18.73% | $1,502,938.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.25% | +2.41% |
| UB/USDT:USDT | below_1h_threshold | +1.96% | +2.12% |
| H/USDT:USDT | below_1h_threshold | +1.33% | +1.49% |
| NOWSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.27% |
| GUA/USDT:USDT | below_1h_threshold | +0.82% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
