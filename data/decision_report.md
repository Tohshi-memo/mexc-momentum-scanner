# Decision Report

- generated_at: 2026-08-31T17:06:26.344443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13191**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13191, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 7/20 | 35.0% | -0.07% | **-0.02%** |
| LIMIT_BB3S | 2/18 | 11.1% | -0.98% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.07% | **+5.07%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.33% | **+2.21%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.35% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.58% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4876件 (Win 1485 / Loss 1609 / Flat 1782) / skip 4876件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.87** / 初期 $100.00 (+73.87%)
- 確定: 2187件 (Win 607 / Loss 528 / Flat 1052) / skip 4415件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOGS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2578件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-08-31T17:06:13.469221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78653.8
- Funnel: target 1031 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +14.25% | $4,231,311.48 |
| DOGS/USDT:USDT | +13.02% | $1,532,615.58 |
| FONE/USDT:USDT | +7.11% | $1,351,167.19 |
| DASH/USDT:USDT | +6.14% | $12,470,886.37 |
| 0G/USDT:USDT | +5.21% | $7,611,472.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +3.96% | +3.90% |
| 0G/USDT:USDT | below_1h_threshold | +2.95% | +2.89% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.34% |
| FONE/USDT:USDT | below_1h_threshold | +1.44% | +1.38% |
| SOXL/USDT:USDT | below_1h_threshold | +1.32% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
