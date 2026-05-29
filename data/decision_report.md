# Decision Report

- generated_at: 2026-05-29T13:39:42.750502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5048**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5048, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.14% | **-0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.13% | **-0.05%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.10% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.49% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.81% | **+0.90%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.99% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$99.09** / 初期 $100.00 (-0.91%)
- 確定トレード: 73件 (TP 22 / SL 48 / EXP 3)
- 最新: NIL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 869件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T13:39:39.517599+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=73152.8
- Funnel: target 777 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +138.33% | $111,509,508.52 |
| HEI/USDT:USDT | +88.12% | $1,139,586.88 |
| ID/USDT:USDT | +34.59% | $2,358,847.21 |
| DELLSTOCK/USDT:USDT | +30.56% | $10,620,007.79 |
| LAB/USDT:USDT | +27.39% | $89,506,661.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.82% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.51% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.90% | +2.05% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.44% |
| NEAR/USDT:USDT | below_1h_threshold | +0.95% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
