# Decision Report

- generated_at: 2026-08-31T17:51:24.220514+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13194**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13194, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/17 | 11.8% | -0.98% | **-0.11%** |
| LIMIT_ATR | 8/20 | 40.0% | -0.36% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.07% | **+3.38%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.81% | **+2.67%** |
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.58% | **+1.42%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.20% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4876件 (Win 1485 / Loss 1609 / Flat 1782) / skip 4879件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.99** / 初期 $100.00 (+73.99%)
- 確定: 2190件 (Win 608 / Loss 528 / Flat 1054) / skip 4415件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2581件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000384 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-08-31T17:51:11.999252+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=78849.2
- Funnel: target 1031 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +14.41% | $6,899,249.93 |
| 0G/USDT:USDT | +13.98% | $10,258,135.90 |
| DOGS/USDT:USDT | +9.18% | $1,877,990.93 |
| DASH/USDT:USDT | +8.54% | $14,262,423.39 |
| ARB/USDT:USDT | +5.91% | $5,403,096.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.30% | +2.99% |
| HEMI/USDT:USDT | below_1h_threshold | +3.11% | +2.80% |
| PONS/USDT:USDT | below_1h_threshold | +3.02% | +2.71% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.09% |
| NOT/USDT:USDT | below_1h_threshold | +2.33% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
