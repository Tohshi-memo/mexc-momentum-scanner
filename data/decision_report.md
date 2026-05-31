# Decision Report

- generated_at: 2026-05-31T17:41:31.405410+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5210**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5210, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.27% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.78% | **+2.08%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.02% | **+1.96%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.79% | **+1.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.23** / 初期 $100.00 (+29.23%)
- 確定: 845件 (Win 196 / Loss 252 / Flat 397) / skip 926件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $129.23

## 4. Latest Market Context

- 更新: 2026-05-31T17:41:26.468248+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=73662.6
- Funnel: target 773 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +10.44% | $6,230,602.55 |
| PORTAL/USDT:USDT | +10.38% | $10,912,084.81 |
| GUA/USDT:USDT | +3.46% | $1,724,686.08 |
| HOME/USDT:USDT | +3.37% | $1,917,179.10 |
| AIA/USDT:USDT | +3.27% | $5,644,234.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.44% | +4.22% |
| LIT/USDT:USDT | below_1h_threshold | +2.58% | +2.36% |
| CHIP/USDT:USDT | below_1h_threshold | +2.01% | +1.79% |
| JUP/USDT:USDT | below_1h_threshold | +1.87% | +1.64% |
| BILL/USDT:USDT | below_1h_threshold | +1.80% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
