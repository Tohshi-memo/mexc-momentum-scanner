# Decision Report

- generated_at: 2026-05-31T01:20:33.651277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5159**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5159, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.78% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.24% | **+1.56%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.51% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.29% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 797件 (Win 184 / Loss 243 / Flat 370) / skip 923件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NFP/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T01:20:31.168247+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=74139.1
- Funnel: target 773 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +58.63% | $7,707,979.32 |
| TA/USDT:USDT | +29.99% | $2,082,863.85 |
| STG/USDT:USDT | +17.40% | $3,631,883.34 |
| ONDO/USDT:USDT | +11.38% | $35,276,078.60 |
| BIANRENSHENG/USDT:USDT | +9.38% | $1,402,200.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_relative_strength | +5.05% | +4.86% |
| ID/USDT:USDT | below_1h_threshold | +3.86% | +3.68% |
| STG/USDT:USDT | below_1h_threshold | +2.48% | +2.30% |
| ZEC/USDT:USDT | below_1h_threshold | +0.95% | +0.77% |
| LIT/USDT:USDT | below_1h_threshold | +0.91% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
