# Decision Report

- generated_at: 2026-07-05T17:28:52.354690+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8340**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8340, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_BB3S | 7/17 | 41.2% | -0.59% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.10% | **+0.72%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 65件 (TP 22 / SL 42 / EXP 1)
- 最新: MAGMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.94** / 初期 $100.00 (+221.94%)
- 確定: 2620件 (Win 832 / Loss 884 / Flat 904) / skip 2281件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $321.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1113件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T17:28:47.279222+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62667.9
- Funnel: target 835 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +11.33% | $4,470,067.20 |
| ZEROC0MPUTE/USDT:USDT | +8.96% | $1,107,458.31 |
| TRB/USDT:USDT | +7.07% | $1,114,034.25 |
| XTZ/USDT:USDT | +4.33% | $1,747,905.36 |
| VELVET/USDT:USDT | +4.07% | $14,379,542.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRB/USDT:USDT | below_1h_threshold | +3.48% | +3.39% |
| NES/USDT:USDT | below_1h_threshold | +3.15% | +3.06% |
| XTZ/USDT:USDT | below_1h_threshold | +2.38% | +2.29% |
| ZEROC0MPUTE/USDT:USDT | below_1h_threshold | +1.90% | +1.81% |
| VELVET/USDT:USDT | below_1h_threshold | +1.40% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
