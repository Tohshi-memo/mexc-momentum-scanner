# Decision Report

- generated_at: 2026-07-05T19:18:10.149691+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8349**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8349, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/13 | 53.8% | +0.04% | **+0.02%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | -0.32% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK_LONG | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT_LONG | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +0.92% | **+0.32%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.71% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 65件 (TP 22 / SL 42 / EXP 1)
- 最新: MAGMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.94** / 初期 $100.00 (+221.94%)
- 確定: 2620件 (Win 832 / Loss 884 / Flat 904) / skip 2290件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $321.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1122件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T19:18:04.935770+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62813.4
- Funnel: target 835 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +16.80% | $33,717,380.83 |
| ZEROC0MPUTE/USDT:USDT | +16.42% | $1,718,220.22 |
| TRB/USDT:USDT | +13.28% | $2,712,681.78 |
| CAP/USDT:USDT | +9.30% | $6,866,712.45 |
| VELVET/USDT:USDT | +9.24% | $14,942,852.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.17% | +2.13% |
| TRB/USDT:USDT | below_1h_threshold | +2.09% | +2.05% |
| VVV/USDT:USDT | below_1h_threshold | +1.67% | +1.63% |
| LDO/USDT:USDT | below_1h_threshold | +1.36% | +1.32% |
| ALLO/USDT:USDT | below_1h_threshold | +1.14% | +1.09% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
