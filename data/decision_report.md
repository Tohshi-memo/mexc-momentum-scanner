# Decision Report

- generated_at: 2026-05-24T01:39:39.000497+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4805**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4805, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.07% | **-0.06%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.09% | **-0.07%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.39% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| ASK_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.60% | **+1.36%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.82%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 750件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-24T01:39:36.321441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=76874.5
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +18.34% | $7,553,268.18 |
| BLUAI/USDT:USDT | +16.57% | $1,807,910.29 |
| NIL/USDT:USDT | +15.86% | $1,902,022.06 |
| IN/USDT:USDT | +11.55% | $3,707,821.25 |
| EIGEN/USDT:USDT | +10.05% | $2,770,187.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.64% | +3.56% |
| NIL/USDT:USDT | below_1h_threshold | +2.65% | +2.57% |
| HYPE/USDT:USDT | below_1h_threshold | +2.36% | +2.28% |
| CHZ/USDT:USDT | below_1h_threshold | +1.80% | +1.72% |
| GRASS/USDT:USDT | below_1h_threshold | +1.74% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
