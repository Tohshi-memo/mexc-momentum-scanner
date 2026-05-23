# Decision Report

- generated_at: 2026-05-23T18:54:09.114487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4796**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4796, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.08% | **-0.04%** |
| LIMIT_BB3S | 5/20 | 25.0% | -0.48% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.91% | **+2.04%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.38% | **+1.86%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 741件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T18:54:06.852570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=75809.8
- Funnel: target 764 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +14.28% | $19,829,794.19 |
| GRASS/USDT:USDT | +9.06% | $4,145,814.39 |
| WLD/USDT:USDT | +8.71% | $44,487,818.98 |
| ME/USDT:USDT | +8.64% | $1,345,414.43 |
| NEAR/USDT:USDT | +6.64% | $140,039,112.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.49% | +4.03% |
| BILL/USDT:USDT | below_1h_threshold | +4.22% | +3.75% |
| LIT/USDT:USDT | below_1h_threshold | +3.97% | +3.50% |
| TIA/USDT:USDT | below_1h_threshold | +3.12% | +2.65% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.85% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
