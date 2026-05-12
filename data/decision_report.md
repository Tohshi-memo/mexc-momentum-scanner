# Decision Report

- generated_at: 2026-05-12T11:47:58.382293+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4114**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4114, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.39% | **-0.14%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.57% | **-0.43%** |
| LIMIT_2PCT | 16/20 | 80.0% | -0.84% | **-0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.54% | **+1.08%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.92% | **+1.06%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.80% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$114.20** / 初期 $100.00 (+14.20%)
- 確定: 250件 (Win 68 / Loss 86 / Flat 96) / skip 425件
- 成長率目線: 平均log +0.000531 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $114.20

## 4. Latest Market Context

- 更新: 2026-05-12T11:47:54.347615+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80705.2
- Funnel: target 763 → liquid 192 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 89.6 >= 65=1, 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +49.71% | $6,049,873.45 |
| SAGA/USDT:USDT | +49.52% | $15,907,476.85 |
| SKYAI/USDT:USDT | +38.65% | $44,095,749.80 |
| USELESS/USDT:USDT | +34.66% | $8,897,583.32 |
| GUA/USDT:USDT | +31.59% | $3,442,856.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JELLYJELLY/USDT:USDT | below_1h_threshold | +1.75% | +1.66% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.74% | +1.65% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.55% | +1.46% |
| AKT/USDT:USDT | below_1h_threshold | +1.50% | +1.41% |
| H/USDT:USDT | below_1h_threshold | +1.34% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
