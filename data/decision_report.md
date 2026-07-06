# Decision Report

- generated_at: 2026-07-06T09:54:25.424122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8380**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.65% / filled 20/20。**
- 全期間 MARKET基準: n=8380, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.84% | **+1.56%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.46% | **+1.10%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.49% | **+0.30%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.01% | **+0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2623件 (Win 832 / Loss 887 / Flat 904) / skip 2318件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1152件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T09:54:18.875306+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=62668.7
- Funnel: target 841 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +25.05% | $6,997,907.31 |
| ZEROC0MPUTE/USDT:USDT | +17.15% | $1,591,192.30 |
| BEL/USDT:USDT | +14.40% | $1,790,090.15 |
| DEXE/USDT:USDT | +12.92% | $1,236,836.97 |
| TRB/USDT:USDT | +11.45% | $12,141,576.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEL/USDT:USDT | below_1h_threshold | +3.32% | +3.65% |
| TLM/USDT:USDT | below_1h_threshold | +2.86% | +3.19% |
| IMX/USDT:USDT | below_1h_threshold | +2.43% | +2.76% |
| GOAT/USDT:USDT | below_1h_threshold | +1.76% | +2.09% |
| PYTH/USDT:USDT | below_1h_threshold | +1.64% | +1.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
