# Decision Report

- generated_at: 2026-05-20T12:53:47.004970+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4544**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=4544, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.35% | **+0.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.72% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.11% | **-0.04%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.18** / 初期 $100.00 (-2.82%)
- 確定トレード: 56件 (TP 15 / SL 38 / EXP 3)
- 最新: SATO/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.91** / 初期 $100.00 (+23.91%)
- 確定: 506件 (Win 132 / Loss 174 / Flat 200) / skip 599件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $123.91

## 4. Latest Market Context

- 更新: 2026-05-20T12:53:44.124174+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=77545.6
- Funnel: target 763 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +84.80% | $2,295,615.75 |
| FIDA/USDT:USDT | +48.01% | $3,953,380.24 |
| PLAY/USDT:USDT | +31.66% | $11,306,164.41 |
| BANANAS31/USDT:USDT | +29.48% | $2,208,667.69 |
| PROMPT/USDT:USDT | +26.06% | $12,785,102.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +4.56% | +4.31% |
| ZEST/USDT:USDT | below_1h_threshold | +3.73% | +3.48% |
| PLAY/USDT:USDT | below_1h_threshold | +3.13% | +2.88% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.86% | +2.61% |
| PENGU/USDT:USDT | below_1h_threshold | +1.99% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
