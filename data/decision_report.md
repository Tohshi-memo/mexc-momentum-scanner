# Decision Report

- generated_at: 2026-05-24T01:59:15.539681+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4806**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4806, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.15% | **-0.12%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.42% | **-0.17%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.66% | **-0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| ASK_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.95% | **+1.56%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.02%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.71% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 751件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-24T01:59:13.245892+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76844.5
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +18.60% | $7,771,620.71 |
| BLUAI/USDT:USDT | +16.19% | $1,810,576.94 |
| NIL/USDT:USDT | +15.12% | $1,935,931.91 |
| IN/USDT:USDT | +9.87% | $3,799,769.99 |
| EIGEN/USDT:USDT | +8.07% | $2,807,164.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.83% | +2.79% |
| NIL/USDT:USDT | below_1h_threshold | +2.00% | +1.95% |
| GRASS/USDT:USDT | below_1h_threshold | +1.97% | +1.92% |
| UB/USDT:USDT | below_1h_threshold | +1.53% | +1.49% |
| MYX/USDT:USDT | below_1h_threshold | +1.53% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
