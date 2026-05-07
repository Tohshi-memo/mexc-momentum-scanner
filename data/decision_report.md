# Decision Report

- generated_at: 2026-05-07T12:57:43.084109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3628**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=3628, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +4.45% | **+1.78%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.23% | **+1.77%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.95% | **+1.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.31% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.74** / 初期 $100.00 (+7.74%)
- 確定: 122件 (Win 39 / Loss 48 / Flat 35) / skip 67件
- 成長率目線: 平均log +0.000611 / 幾何平均 +0.061% per trade / maxDD +2.62%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.56% 残高後 $107.74

## 4. Latest Market Context

- 更新: 2026-05-07T12:57:39.238221+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=81079.8
- Funnel: target 771 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1, 4h RSI 90.4 >= 65=1, 4h RSI 81.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +98.19% | $12,048,273.77 |
| PENGUIN/USDT:USDT | +68.54% | $3,907,862.06 |
| SATO/USDT:USDT | +66.81% | $2,823,088.15 |
| DOGS/USDT:USDT | +52.39% | $16,737,397.73 |
| NIL/USDT:USDT | +35.41% | $3,381,830.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POPCAT/USDT:USDT | below_1h_threshold | +4.04% | +3.73% |
| BILL/USDT:USDT | below_1h_threshold | +4.01% | +3.70% |
| BRETT/USDT:USDT | below_1h_threshold | +3.29% | +2.98% |
| STRK/USDT:USDT | below_1h_threshold | +2.61% | +2.30% |
| ICP/USDT:USDT | below_1h_threshold | +2.42% | +2.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
