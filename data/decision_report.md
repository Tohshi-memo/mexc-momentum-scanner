# Decision Report

- generated_at: 2026-05-31T00:54:49.616045+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5158**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5158, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.48% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.82% | **+1.36%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.41% | **+1.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.76%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.65% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 796件 (Win 184 / Loss 243 / Flat 369) / skip 923件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +6.32%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T00:54:45.715005+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=73988.6
- Funnel: target 773 → liquid 121 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.0 >= 65=1, 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +57.16% | $7,073,172.10 |
| TA/USDT:USDT | +23.16% | $2,045,013.69 |
| STG/USDT:USDT | +15.82% | $3,489,335.36 |
| ONDO/USDT:USDT | +12.28% | $34,763,921.35 |
| BIANRENSHENG/USDT:USDT | +11.71% | $1,391,681.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +4.22% | +4.04% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.45% | +3.27% |
| TA/USDT:USDT | below_1h_threshold | +2.74% | +2.56% |
| ONDO/USDT:USDT | below_1h_threshold | +2.45% | +2.27% |
| AXS/USDT:USDT | below_1h_threshold | +2.43% | +2.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
