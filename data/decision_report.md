# Decision Report

- generated_at: 2026-05-07T02:47:52.952143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3536**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3536, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.66% | **-1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.74% | **+0.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.73% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.62% | **+1.99%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.44% | **+1.95%** |
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.90% | **+1.31%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.79% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定: 31件 (Win 10 / Loss 13 / Flat 8) / skip 66件
- 成長率目線: 平均log +0.000518 / 幾何平均 +0.052% per trade / maxDD +2.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $101.62

## 4. Latest Market Context

- 更新: 2026-05-07T02:47:49.244308+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81020.0
- Funnel: target 770 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 82.5 >= 65=1, 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +199.50% | $1,144,089.63 |
| DOGS/USDT:USDT | +77.80% | $8,004,422.13 |
| PENGUIN/USDT:USDT | +33.00% | $1,148,090.45 |
| FHE/USDT:USDT | +32.40% | $16,225,785.04 |
| LAB/USDT:USDT | +15.03% | $259,748,959.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.89% | +4.01% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.96% | +3.09% |
| LAB/USDT:USDT | below_1h_threshold | +2.66% | +2.78% |
| ORCA/USDT:USDT | below_1h_threshold | +2.63% | +2.75% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.52% | +2.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
