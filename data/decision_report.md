# Decision Report

- generated_at: 2026-05-12T13:27:58.789335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4122**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4122, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.12% | **+0.06%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.51% | **+1.26%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.11% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.06** / 初期 $100.00 (+15.06%)
- 確定: 258件 (Win 70 / Loss 88 / Flat 100) / skip 425件
- 成長率目線: 平均log +0.000544 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.06

## 4. Latest Market Context

- 更新: 2026-05-12T13:27:55.050232+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=80613.9
- Funnel: target 763 → liquid 193 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1, 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +84.57% | $22,638,650.67 |
| GIGA/USDT:USDT | +57.75% | $6,817,429.97 |
| USELESS/USDT:USDT | +42.16% | $10,053,547.44 |
| SKYAI/USDT:USDT | +38.92% | $43,663,793.29 |
| GUA/USDT:USDT | +34.38% | $3,610,476.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOLV/USDT:USDT | below_1h_threshold | +4.58% | +4.87% |
| USELESS/USDT:USDT | below_1h_threshold | +3.73% | +4.02% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.72% | +3.01% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.28% | +2.57% |
| H/USDT:USDT | below_1h_threshold | +2.21% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
