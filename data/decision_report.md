# Decision Report

- generated_at: 2026-05-20T14:23:58.351646+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4546**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=4546, expectancy=-0.09%
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
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.00% | **+0.90%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.72% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.22% | **-0.09%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.18** / 初期 $100.00 (-2.82%)
- 確定トレード: 56件 (TP 15 / SL 38 / EXP 3)
- 最新: SATO/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.06** / 初期 $100.00 (+24.06%)
- 確定: 508件 (Win 133 / Loss 174 / Flat 201) / skip 599件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $124.06

## 4. Latest Market Context

- 更新: 2026-05-20T14:23:55.781820+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=77389.0
- Funnel: target 763 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +80.11% | $2,622,391.55 |
| FIDA/USDT:USDT | +57.50% | $5,183,788.76 |
| BANANAS31/USDT:USDT | +26.85% | $2,946,907.90 |
| PROMPT/USDT:USDT | +25.49% | $12,883,109.15 |
| LIT/USDT:USDT | +24.63% | $10,464,236.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.26% | +3.98% |
| ZEC/USDT:USDT | below_1h_threshold | +3.22% | +2.95% |
| DASH/USDT:USDT | below_1h_threshold | +2.61% | +2.34% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.37% | +2.09% |
| STRK/USDT:USDT | below_1h_threshold | +2.09% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
