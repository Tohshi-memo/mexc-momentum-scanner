# Decision Report

- generated_at: 2026-05-08T05:57:46.684376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3741**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=3741, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.23% | **+0.98%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 25件 (TP 6 / SL 17 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 112件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T05:57:42.503478+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79618.9
- Funnel: target 772 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +42.99% | $3,120,272.02 |
| BSB/USDT:USDT | +22.87% | $4,552,371.08 |
| LAB/USDT:USDT | +18.99% | $213,952,911.66 |
| NOT/USDT:USDT | +18.54% | $10,615,534.27 |
| TST/USDT:USDT | +12.69% | $6,488,680.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.96% | +2.96% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +2.96% | +2.96% |
| ICP/USDT:USDT | below_1h_threshold | +2.33% | +2.33% |
| MOVR/USDT:USDT | below_1h_threshold | +2.26% | +2.26% |
| STRK/USDT:USDT | below_1h_threshold | +1.88% | +1.88% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
