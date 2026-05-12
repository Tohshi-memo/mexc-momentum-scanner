# Decision Report

- generated_at: 2026-05-12T02:03:04.363877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4089**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4089, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.60% | **+0.65%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.42% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.45** / 初期 $100.00 (+11.45%)
- 確定: 226件 (Win 59 / Loss 78 / Flat 89) / skip 424件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $111.45

## 4. Latest Market Context

- 更新: 2026-05-12T02:02:58.271113+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=81221.6
- Funnel: target 762 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +55.79% | $1,548,555.00 |
| SKYAI/USDT:USDT | +33.68% | $38,274,215.44 |
| USELESS/USDT:USDT | +22.32% | $4,048,635.13 |
| SAGA/USDT:USDT | +17.25% | $7,244,658.96 |
| H/USDT:USDT | +16.43% | $15,833,020.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +2.13% | +2.04% |
| ONDO/USDT:USDT | below_1h_threshold | +1.64% | +1.55% |
| ROBO/USDT:USDT | below_1h_threshold | +0.81% | +0.72% |
| USELESS/USDT:USDT | below_1h_threshold | +0.80% | +0.71% |
| JTO/USDT:USDT | below_1h_threshold | +0.73% | +0.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
