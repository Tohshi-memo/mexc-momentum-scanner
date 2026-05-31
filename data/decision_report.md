# Decision Report

- generated_at: 2026-05-31T17:01:03.864220+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5208**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5208, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.27% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.69% | **+1.48%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.54% | **+0.93%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.89% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.95** / 初期 $100.00 (+28.95%)
- 確定: 843件 (Win 195 / Loss 251 / Flat 397) / skip 926件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $128.95

## 4. Latest Market Context

- 更新: 2026-05-31T17:01:01.391292+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=73510.0
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +12.11% | $10,104,173.17 |
| STG/USDT:USDT | +5.71% | $5,473,366.19 |
| AIA/USDT:USDT | +5.40% | $5,509,327.77 |
| HOME/USDT:USDT | +4.88% | $1,728,926.13 |
| ALLO/USDT:USDT | +2.45% | $28,048,871.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEX/USDT:USDT | below_1h_threshold | +1.26% | +1.24% |
| HOME/USDT:USDT | below_1h_threshold | +0.78% | +0.77% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| SIGN/USDT:USDT | below_1h_threshold | +0.43% | +0.42% |
| JUP/USDT:USDT | below_1h_threshold | +0.38% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
