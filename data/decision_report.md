# Decision Report

- generated_at: 2026-05-17T21:18:24.738779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4422**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4422, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 4/13 | 30.8% | +1.43% | **+0.44%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.30% | **-0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.53% | **+1.65%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.21% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.58** / 初期 $100.00 (+22.58%)
- 確定: 419件 (Win 110 / Loss 141 / Flat 168) / skip 564件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $122.58

## 4. Latest Market Context

- 更新: 2026-05-17T21:18:22.545809+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=78227.8
- Funnel: target 760 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +18.20% | $1,279,487.33 |
| FIDA/USDT:USDT | +17.18% | $2,735,302.48 |
| UB/USDT:USDT | +10.93% | $13,913,733.98 |
| BILL/USDT:USDT | +7.87% | $33,985,881.81 |
| HYPE/USDT:USDT | +7.38% | $270,348,325.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.39% | +2.39% |
| AKT/USDT:USDT | below_1h_threshold | +1.61% | +1.61% |
| ZEC/USDT:USDT | below_1h_threshold | +1.56% | +1.56% |
| B/USDT:USDT | below_1h_threshold | +1.31% | +1.31% |
| RIVER/USDT:USDT | below_1h_threshold | +1.03% | +1.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
