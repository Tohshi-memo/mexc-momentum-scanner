# Decision Report

- generated_at: 2026-06-16T09:11:02.144558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6853**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6853, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.57% | **+0.16%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.03% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| ASK_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.79% | **+0.63%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$182.90** / 初期 $100.00 (+82.90%)
- 確定: 1726件 (Win 449 / Loss 538 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $182.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 108件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0236 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T09:10:58.049355+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=66729.1
- Funnel: target 777 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +72.16% | $4,704,311.85 |
| BR/USDT:USDT | +46.72% | $1,293,060.37 |
| BSB/USDT:USDT | +35.86% | $28,061,386.33 |
| VELVET/USDT:USDT | +35.82% | $16,985,773.46 |
| ASTEROID/USDT:USDT | +31.28% | $4,728,474.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.15% | +3.34% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.78% | +2.96% |
| STG/USDT:USDT | below_1h_threshold | +1.92% | +2.11% |
| LAB/USDT:USDT | below_1h_threshold | +1.48% | +1.67% |
| PUFFER/USDT:USDT | below_1h_threshold | +1.40% | +1.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
