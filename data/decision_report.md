# Decision Report

- generated_at: 2026-05-28T13:54:53.508020+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4963**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=4963, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.79% | **+1.43%** |
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.18% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.15% | **-0.06%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.66% | **-0.30%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | -0.66% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 698件 (Win 172 / Loss 220 / Flat 306) / skip 826件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDSSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T13:54:48.424318+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.78% price=72923.9
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +32.65% | $11,195,088.31 |
| ONDSSTOCK/USDT:USDT | +25.28% | $1,145,409.93 |
| XLM/USDT:USDT | +23.18% | $198,637,474.70 |
| PRL/USDT:USDT | +16.78% | $2,412,490.13 |
| NBISSTOCK/USDT:USDT | +10.43% | $2,138,438.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +4.64% | +5.41% |
| CRO/USDT:USDT | below_1h_threshold | +2.51% | +3.29% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.00% | +2.78% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +1.74% | +2.52% |
| PI/USDT:USDT | below_1h_threshold | +0.63% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
