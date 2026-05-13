# Decision Report

- generated_at: 2026-05-13T06:58:04.909472+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4192**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=4192, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.86% | **+1.67%** |
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.85% | **+1.30%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.28% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.22% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.57** / 初期 $100.00 (+19.57%)
- 確定: 328件 (Win 92 / Loss 117 / Flat 119) / skip 425件
- 成長率目線: 平均log +0.000545 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $119.57

## 4. Latest Market Context

- 更新: 2026-05-13T06:58:01.578373+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80945.6
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +38.82% | $5,309,669.51 |
| SATO/USDT:USDT | +23.09% | $1,251,661.04 |
| LAB/USDT:USDT | +19.10% | $109,584,591.12 |
| PEAQ/USDT:USDT | +19.07% | $2,605,883.12 |
| INJ/USDT:USDT | +13.73% | $57,856,798.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +3.43% | +3.48% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.06% | +3.11% |
| KITE/USDT:USDT | below_1h_threshold | +2.79% | +2.84% |
| UB/USDT:USDT | below_1h_threshold | +2.35% | +2.40% |
| ROSE/USDT:USDT | below_1h_threshold | +1.68% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
