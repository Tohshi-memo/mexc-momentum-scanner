# Decision Report

- generated_at: 2026-05-26T15:24:26.911429+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4903**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=4903, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| ASK | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.47% | **+1.32%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.11% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.49% | **+0.52%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.25% | **+0.19%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.22** / 初期 $100.00 (+29.22%)
- 確定: 677件 (Win 171 / Loss 215 / Flat 291) / skip 787件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $129.22

## 4. Latest Market Context

- 更新: 2026-05-26T15:24:24.741862+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=76680.0
- Funnel: target 769 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +59.28% | $3,004,992.72 |
| WLD/USDT:USDT | +30.34% | $178,646,958.43 |
| DRIFT/USDT:USDT | +22.25% | $4,066,197.70 |
| IO/USDT:USDT | +15.12% | $1,366,944.22 |
| OKB/USDT:USDT | +13.95% | $1,756,916.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +3.38% | +3.63% |
| WLD/USDT:USDT | below_1h_threshold | +1.31% | +1.56% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.19% | +1.45% |
| UB/USDT:USDT | below_1h_threshold | +0.87% | +1.12% |
| H/USDT:USDT | below_1h_threshold | +0.75% | +1.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
