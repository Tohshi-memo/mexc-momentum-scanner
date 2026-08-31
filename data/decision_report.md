# Decision Report

- generated_at: 2026-08-31T19:01:24.011444+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13200**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13200, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.62% | **-0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 10/20 | 50.0% | -0.22% | **-0.11%** |
| LIMIT_BB3S | 3/15 | 20.0% | -0.70% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.85% | **+1.67%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.66% | **+1.60%** |
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.03% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4877件 (Win 1485 / Loss 1609 / Flat 1783) / skip 4884件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.99** / 初期 $100.00 (+73.99%)
- 確定: 2192件 (Win 608 / Loss 528 / Flat 1056) / skip 4419件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2587件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-08-31T19:01:14.730616+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79028.3
- Funnel: target 1031 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +18.22% | $8,970,112.05 |
| FONE/USDT:USDT | +16.69% | $1,177,040.57 |
| HEMI/USDT:USDT | +14.54% | $9,313,195.06 |
| 0G/USDT:USDT | +12.28% | $12,458,979.95 |
| DOGS/USDT:USDT | +10.63% | $2,315,035.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.31% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.56% |
| ZORA/USDT:USDT | below_1h_threshold | +0.48% | +0.42% |
| ARB/USDT:USDT | below_1h_threshold | +0.36% | +0.30% |
| MONAD/USDT:USDT | below_1h_threshold | +0.29% | +0.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
