# Decision Report

- generated_at: 2026-05-17T06:48:26.436238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4389**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4389, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.60% | **+0.65%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.25% | **+0.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.07% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.60% | **+0.96%** |
| ASK_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.75% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 557件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T06:48:20.284909+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=78015.5
- Funnel: target 760 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +35.20% | $8,631,284.36 |
| CGPT/USDT:USDT | +29.36% | $1,907,514.07 |
| ASTEROID/USDT:USDT | +21.46% | $4,439,481.52 |
| BSB/USDT:USDT | +20.19% | $4,720,542.90 |
| UP/USDT:USDT | +9.17% | $1,504,574.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.38% | +3.47% |
| LUNC/USDT:USDT | below_1h_threshold | +2.81% | +2.90% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.37% | +2.47% |
| BSB/USDT:USDT | below_1h_threshold | +2.13% | +2.23% |
| LAB/USDT:USDT | below_1h_threshold | +1.38% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
