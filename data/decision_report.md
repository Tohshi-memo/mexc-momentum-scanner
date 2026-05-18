# Decision Report

- generated_at: 2026-05-18T10:53:37.739271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4439**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=4439, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.70% | **+0.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.27% | **+0.17%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.78% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.22** / 初期 $100.00 (-3.78%)
- 確定トレード: 52件 (TP 13 / SL 36 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 436件 (Win 114 / Loss 148 / Flat 174) / skip 564件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $122.02

## 4. Latest Market Context

- 更新: 2026-05-18T10:53:33.027295+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=76816.9
- Funnel: target 768 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRAC/USDT:USDT | +49.26% | $1,009,812.37 |
| FIDA/USDT:USDT | +42.62% | $8,798,867.88 |
| BSB/USDT:USDT | +14.56% | $20,843,024.80 |
| OPENLEDGER/USDT:USDT | +9.25% | $1,424,325.56 |
| RIVER/USDT:USDT | +4.56% | $9,357,547.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +2.63% | +2.74% |
| OPENLEDGER/USDT:USDT | below_1h_threshold | +2.38% | +2.49% |
| LAB/USDT:USDT | below_1h_threshold | +1.88% | +1.99% |
| NEAR/USDT:USDT | below_1h_threshold | +1.82% | +1.93% |
| RIVER/USDT:USDT | below_1h_threshold | +1.54% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
