# Decision Report

- generated_at: 2026-08-31T17:16:19.080128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13192**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13192, expectancy=+0.01%
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
| LIMIT_ATR | 7/20 | 35.0% | -0.20% | **-0.07%** |
| LIMIT_BB3S | 2/17 | 11.8% | -0.98% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.07% | **+3.38%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.33% | **+2.21%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.03% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.58% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4876件 (Win 1485 / Loss 1609 / Flat 1782) / skip 4877件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.87** / 初期 $100.00 (+73.87%)
- 確定: 2188件 (Win 607 / Loss 528 / Flat 1053) / skip 4415件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2578件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-08-31T17:16:09.584730+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78665.5
- Funnel: target 1031 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +15.56% | $4,718,943.07 |
| FONE/USDT:USDT | +10.62% | $1,357,040.73 |
| DOGS/USDT:USDT | +8.65% | $1,611,027.61 |
| 0G/USDT:USDT | +7.60% | $7,902,423.23 |
| DASH/USDT:USDT | +6.90% | $12,654,576.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 0G/USDT:USDT | below_relative_strength | +5.05% | +4.97% |
| FONE/USDT:USDT | below_1h_threshold | +4.76% | +4.69% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.33% |
| PONS/USDT:USDT | below_1h_threshold | +2.31% | +2.23% |
| MUU/USDT:USDT | below_1h_threshold | +2.03% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
