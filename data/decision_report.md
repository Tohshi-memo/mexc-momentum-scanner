# Decision Report

- generated_at: 2026-05-12T20:43:05.073937+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4159**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4159, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.14% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.36% | **+2.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.11% | **+1.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定: 295件 (Win 85 / Loss 101 / Flat 109) / skip 425件
- 成長率目線: 平均log +0.000634 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.56

## 4. Latest Market Context

- 更新: 2026-05-12T20:43:01.225360+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=80620.0
- Funnel: target 758 → liquid 191 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.7 >= 65=1, 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +22.40% | $53,260,624.49 |
| DYM/USDT:USDT | +12.42% | $2,059,886.27 |
| SATO/USDT:USDT | +12.35% | $1,118,121.42 |
| VIC/USDT:USDT | +11.64% | $5,776,828.91 |
| LAB/USDT:USDT | +11.21% | $136,048,726.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.37% | +4.59% |
| SATO/USDT:USDT | below_1h_threshold | +3.31% | +3.53% |
| GIGA/USDT:USDT | below_1h_threshold | +3.00% | +3.22% |
| STX/USDT:USDT | below_1h_threshold | +1.82% | +2.04% |
| KITE/USDT:USDT | below_1h_threshold | +1.58% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
