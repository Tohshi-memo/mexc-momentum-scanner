# Decision Report

- generated_at: 2026-07-08T21:31:10.717706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8507**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8507, expectancy=-0.01%
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
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.51% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.50% | **+0.23%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.19% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$104.10** / 初期 $100.00 (+4.10%)
- 確定トレード: 80件 (TP 29 / SL 50 / EXP 1)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.08** / 初期 $100.00 (+220.08%)
- 確定: 2696件 (Win 852 / Loss 903 / Flat 941) / skip 2372件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $320.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1276件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T21:31:05.562647+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62113.9
- Funnel: target 851 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +59.42% | $2,919,598.65 |
| OGN/USDT:USDT | +23.54% | $3,354,275.72 |
| LAB/USDT:USDT | +15.17% | $57,331,812.92 |
| ALLO/USDT:USDT | +12.65% | $11,487,421.83 |
| BTW/USDT:USDT | +11.10% | $1,302,678.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APE/USDT:USDT | below_1h_threshold | +3.31% | +3.25% |
| LAB/USDT:USDT | below_1h_threshold | +2.38% | +2.31% |
| MYX/USDT:USDT | below_1h_threshold | +2.21% | +2.15% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.07% | +2.01% |
| LIT/USDT:USDT | below_1h_threshold | +1.97% | +1.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
