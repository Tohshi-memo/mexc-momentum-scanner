# Decision Report

- generated_at: 2026-05-31T01:35:36.091455+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5160**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5160, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.78% | **+0.56%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.01% | **+1.81%** |
| ASK_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.79% | **+1.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.51% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 798件 (Win 184 / Loss 243 / Flat 371) / skip 923件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T01:35:31.176375+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=74169.9
- Funnel: target 773 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +53.54% | $7,885,032.28 |
| TA/USDT:USDT | +31.36% | $2,125,353.06 |
| STG/USDT:USDT | +15.21% | $3,659,006.73 |
| ONDO/USDT:USDT | +11.06% | $35,678,576.30 |
| BIANRENSHENG/USDT:USDT | +10.59% | $1,404,733.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +3.20% | +2.97% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.01% | +1.78% |
| ZEC/USDT:USDT | below_1h_threshold | +1.80% | +1.58% |
| AR/USDT:USDT | below_1h_threshold | +1.66% | +1.43% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.54% | +1.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
