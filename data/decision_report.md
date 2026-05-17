# Decision Report

- generated_at: 2026-05-17T04:13:30.550310+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4380**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4380, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.76% | **+0.53%** |
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.62% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.57% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.51% | **+0.38%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.06% | **-0.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.11% | **-0.07%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | -0.58% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$97.19** / 初期 $100.00 (-2.81%)
- 確定トレード: 50件 (TP 13 / SL 34 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -3.29% 残高後 $97.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 548件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T04:13:27.011495+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78006.2
- Funnel: target 760 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +45.65% | $3,915,613.13 |
| CGPT/USDT:USDT | +21.57% | $1,450,073.49 |
| BSB/USDT:USDT | +15.77% | $4,251,816.82 |
| LYN/USDT:USDT | +8.87% | $4,442,084.33 |
| VVV/USDT:USDT | +8.35% | $4,483,864.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +2.70% | +2.68% |
| RUNE/USDT:USDT | below_1h_threshold | +2.46% | +2.44% |
| ZEC/USDT:USDT | below_1h_threshold | +1.60% | +1.58% |
| VVV/USDT:USDT | below_1h_threshold | +1.30% | +1.28% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.25% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
