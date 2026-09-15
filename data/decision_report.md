# Decision Report

- generated_at: 2026-09-15T17:11:23.647806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14605**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14605, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +2.11% | **+0.58%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.86% | **+0.52%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.45% | **+0.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.24% | **+0.11%** |
| MARKET_LONG | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.15% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,069.48** / 初期 $100.00 (+969.48%)
- 確定: 5507件 (Win 1644 / Loss 1779 / Flat 2084) / skip 5659件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWER/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,069.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.23** / 初期 $100.00 (+131.23%)
- 確定: 3045件 (Win 839 / Loss 718 / Flat 1488) / skip 4971件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: POWER/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $231.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3172件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T17:11:12.954813+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=76211.3
- Funnel: target 1060 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +7.17% | $4,544,706.92 |
| SHROOM/USDT:USDT | +7.00% | $2,387,369.81 |
| POWER/USDT:USDT | +4.85% | $14,391,938.32 |
| SAGA/USDT:USDT | +3.37% | $3,060,861.47 |
| 4/USDT:USDT | +3.37% | $1,032,934.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +1.34% | +1.53% |
| USOIL/USDT:USDT | below_1h_threshold | +1.04% | +1.22% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +0.97% | +1.16% |
| ARB/USDT:USDT | below_1h_threshold | +0.94% | +1.12% |
| LSK/USDT:USDT | below_1h_threshold | +0.93% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
