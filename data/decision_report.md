# Decision Report

- generated_at: 2026-05-20T14:43:50.709331+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4548**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=4548, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.74% | **+0.70%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.32% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.36% | **+0.36%** |
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.41% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.32% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.44** / 初期 $100.00 (+23.44%)
- 確定: 510件 (Win 133 / Loss 175 / Flat 202) / skip 599件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.50% 残高後 $123.44

## 4. Latest Market Context

- 更新: 2026-05-20T14:43:47.997601+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=77335.8
- Funnel: target 763 → liquid 131 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1, 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +89.75% | $2,765,165.17 |
| FIDA/USDT:USDT | +58.35% | $5,761,962.63 |
| EDEN/USDT:USDT | +32.85% | $23,597,718.23 |
| BANANAS31/USDT:USDT | +28.28% | $3,091,993.09 |
| LIT/USDT:USDT | +24.83% | $10,710,559.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.45% | +4.24% |
| DASH/USDT:USDT | below_1h_threshold | +3.75% | +3.54% |
| BSB/USDT:USDT | below_1h_threshold | +3.25% | +3.04% |
| ZEN/USDT:USDT | below_1h_threshold | +2.51% | +2.30% |
| STRK/USDT:USDT | below_1h_threshold | +2.45% | +2.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
