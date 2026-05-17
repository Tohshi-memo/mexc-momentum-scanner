# Decision Report

- generated_at: 2026-05-17T03:28:32.214121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4378**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=4378, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.01% | **+0.66%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.70% | **+0.38%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.29% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.51% | **+0.38%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.21% | **-0.07%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.39% | **-0.27%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.84% | **-0.42%** |

## 2. $100 Live Portfolio

- 残高: **$98.17** / 初期 $100.00 (-1.83%)
- 確定トレード: 48件 (TP 13 / SL 32 / EXP 3)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 546件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T03:28:24.530456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77930.8
- Funnel: target 760 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +38.71% | $2,851,038.92 |
| BSB/USDT:USDT | +17.07% | $4,113,407.74 |
| CGPT/USDT:USDT | +15.01% | $1,366,608.96 |
| LYN/USDT:USDT | +8.79% | $4,363,865.59 |
| ASTEROID/USDT:USDT | +6.96% | $4,348,138.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +3.47% | +3.38% |
| AIA/USDT:USDT | below_1h_threshold | +3.12% | +3.02% |
| LAB/USDT:USDT | below_1h_threshold | +3.07% | +2.97% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.22% | +2.13% |
| BSB/USDT:USDT | below_1h_threshold | +2.12% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
