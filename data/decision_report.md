# Decision Report

- generated_at: 2026-05-12T11:32:57.032183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4113**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4113, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.18% | **-0.05%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.55% | **-0.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | -0.68% | **-0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.67% | **+1.25%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.92% | **+1.06%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.46% | **+0.88%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.88% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$114.20** / 初期 $100.00 (+14.20%)
- 確定: 249件 (Win 68 / Loss 86 / Flat 95) / skip 425件
- 成長率目線: 平均log +0.000533 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $114.20

## 4. Latest Market Context

- 更新: 2026-05-12T11:32:53.538567+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80620.0
- Funnel: target 762 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1, 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +51.01% | $15,556,204.19 |
| GIGA/USDT:USDT | +47.20% | $5,945,002.42 |
| SKYAI/USDT:USDT | +39.44% | $43,835,078.39 |
| USELESS/USDT:USDT | +34.25% | $8,786,955.14 |
| GUA/USDT:USDT | +30.95% | $3,417,825.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.97% | +4.99% |
| BILL/USDT:USDT | below_1h_threshold | +1.78% | +1.80% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.70% | +1.71% |
| H/USDT:USDT | below_1h_threshold | +1.06% | +1.08% |
| RUNE/USDT:USDT | below_1h_threshold | +1.04% | +1.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
