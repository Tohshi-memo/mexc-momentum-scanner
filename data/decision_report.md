# Decision Report

- generated_at: 2026-05-17T19:38:29.000867+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4417**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4417, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/12 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.38% | **+1.66%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.17% | **+1.63%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.83% | **+1.00%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.26% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定: 414件 (Win 108 / Loss 140 / Flat 166) / skip 564件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $121.05

## 4. Latest Market Context

- 更新: 2026-05-17T19:38:27.025437+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78200.9
- Funnel: target 760 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +17.36% | $2,152,264.64 |
| BILL/USDT:USDT | +8.32% | $32,804,397.89 |
| UB/USDT:USDT | +7.82% | $13,075,299.76 |
| HYPE/USDT:USDT | +6.20% | $239,015,765.80 |
| ASTEROID/USDT:USDT | +5.60% | $4,094,782.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +2.42% | +2.45% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.11% | +2.14% |
| IONQSTOCK/USDT:USDT | below_1h_threshold | +1.78% | +1.81% |
| HYPE/USDT:USDT | below_1h_threshold | +1.68% | +1.71% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.61% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
