# Decision Report

- generated_at: 2026-05-23T20:59:23.993941+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4799**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4799, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.08% | **-0.04%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.12% | **+2.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.59% | **+2.15%** |
| ASK_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 744件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T20:59:12.996846+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.53% price=77112.3
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=43, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +25.39% | $1,355,695.35 |
| GRASS/USDT:USDT | +16.59% | $4,755,750.10 |
| NIL/USDT:USDT | +12.31% | $1,204,335.22 |
| GUA/USDT:USDT | +10.73% | $1,104,670.32 |
| EIGEN/USDT:USDT | +8.84% | $2,118,399.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_relative_strength | +6.52% | +4.99% |
| DYDX/USDT:USDT | below_relative_strength | +5.21% | +3.68% |
| LIT/USDT:USDT | below_1h_threshold | +4.82% | +3.29% |
| ENA/USDT:USDT | below_1h_threshold | +4.29% | +2.76% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.09% | +2.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
