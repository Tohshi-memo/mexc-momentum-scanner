# Decision Report

- generated_at: 2026-05-12T13:43:08.374637+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4125**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4125, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.21% | **+0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.34% | **+0.94%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.39% | **+0.70%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$114.49** / 初期 $100.00 (+14.49%)
- 確定: 261件 (Win 70 / Loss 89 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000518 / 幾何平均 +0.052% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COLLECT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $114.49

## 4. Latest Market Context

- 更新: 2026-05-12T13:43:04.288418+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=80681.5
- Funnel: target 763 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +86.89% | $24,097,852.27 |
| GIGA/USDT:USDT | +53.68% | $6,941,570.00 |
| USELESS/USDT:USDT | +42.79% | $10,380,253.99 |
| SKYAI/USDT:USDT | +41.47% | $43,923,361.13 |
| GUA/USDT:USDT | +34.73% | $3,638,732.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.48% | +4.68% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.94% | +4.15% |
| GIGA/USDT:USDT | below_1h_threshold | +3.81% | +4.01% |
| USELESS/USDT:USDT | below_1h_threshold | +3.73% | +3.93% |
| H/USDT:USDT | below_1h_threshold | +3.51% | +3.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
