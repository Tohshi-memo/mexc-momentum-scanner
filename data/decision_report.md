# Decision Report

- generated_at: 2026-06-16T09:50:32.881778+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6855**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6855, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.74% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$185.21** / 初期 $100.00 (+85.21%)
- 確定: 1728件 (Win 451 / Loss 538 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $185.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 110件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0508 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T09:50:28.778781+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.56% price=66480.2
- Funnel: target 777 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +71.96% | $5,013,740.74 |
| BR/USDT:USDT | +45.89% | $1,485,499.64 |
| VELVET/USDT:USDT | +41.27% | $17,833,686.94 |
| ASTEROID/USDT:USDT | +33.19% | $4,833,344.88 |
| BSB/USDT:USDT | +32.61% | $30,576,405.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.70% | +4.26% |
| SPACE/USDT:USDT | below_1h_threshold | +3.32% | +3.88% |
| BR/USDT:USDT | below_1h_threshold | +2.57% | +3.13% |
| PLAY/USDT:USDT | below_1h_threshold | +2.35% | +2.91% |
| LAB/USDT:USDT | below_1h_threshold | +2.33% | +2.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
