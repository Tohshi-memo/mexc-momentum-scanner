# Decision Report

- generated_at: 2026-05-07T15:57:46.942287+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3651**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=3651, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.55% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.86% | **+2.00%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.72% | **+1.49%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.05** / 初期 $100.00 (+11.05%)
- 確定: 145件 (Win 45 / Loss 53 / Flat 47) / skip 67件
- 成長率目線: 平均log +0.000723 / 幾何平均 +0.072% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $111.05

## 4. Latest Market Context

- 更新: 2026-05-07T15:57:43.165317+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=79948.7
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1, 4h RSI 75.9 >= 65=1, 4h RSI 93.7 >= 65=1, 4h RSI 73.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +97.10% | $10,502,271.71 |
| SATO/USDT:USDT | +89.47% | $3,973,857.85 |
| PENGUIN/USDT:USDT | +60.02% | $4,547,649.09 |
| NIL/USDT:USDT | +59.21% | $5,896,570.74 |
| DOGS/USDT:USDT | +49.13% | $18,218,351.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| D/USDT:USDT | below_1h_threshold | +3.89% | +4.12% |
| KSM/USDT:USDT | below_1h_threshold | +3.52% | +3.74% |
| STRK/USDT:USDT | below_1h_threshold | +3.40% | +3.62% |
| XPL/USDT:USDT | below_1h_threshold | +2.68% | +2.90% |
| SIREN/USDT:USDT | below_1h_threshold | +1.98% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
