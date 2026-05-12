# Decision Report

- generated_at: 2026-05-12T20:58:02.953523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4162**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4162, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_BB3S | 8/17 | 47.1% | +0.03% | **+0.01%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.13% | **+0.74%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.77% | **+0.70%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定: 298件 (Win 86 / Loss 103 / Flat 109) / skip 425件
- 成長率目線: 平均log +0.000627 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $120.55

## 4. Latest Market Context

- 更新: 2026-05-12T20:57:59.177074+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80646.1
- Funnel: target 758 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.6 >= 65=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +20.18% | $57,759,900.50 |
| DYM/USDT:USDT | +14.06% | $2,182,033.19 |
| PEAQ/USDT:USDT | +12.74% | $2,026,148.18 |
| LAB/USDT:USDT | +11.65% | $137,563,301.29 |
| KITE/USDT:USDT | +9.39% | $2,215,760.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.81% | +5.00% |
| KITE/USDT:USDT | below_1h_threshold | +3.12% | +3.31% |
| PEAQ/USDT:USDT | below_1h_threshold | +3.10% | +3.28% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.60% | +2.79% |
| STX/USDT:USDT | below_1h_threshold | +2.47% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
