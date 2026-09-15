# Decision Report

- generated_at: 2026-09-15T13:26:25.688489+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14597**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14597, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +0.58% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.12% | **+0.62%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.06% | **+0.51%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.07% | **+0.37%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,071.18** / 初期 $100.00 (+971.18%)
- 確定: 5499件 (Win 1642 / Loss 1776 / Flat 2081) / skip 5659件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,071.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.07** / 初期 $100.00 (+131.07%)
- 確定: 3037件 (Win 838 / Loss 718 / Flat 1481) / skip 4971件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $231.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3160件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000091 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T13:26:13.086082+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=76924.7
- Funnel: target 1060 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +61.39% | $15,330,945.95 |
| AKE/USDT:USDT | +60.70% | $16,561,062.34 |
| SHROOM/USDT:USDT | +59.09% | $2,294,938.79 |
| POWER/USDT:USDT | +47.20% | $13,063,138.12 |
| BONER/USDT:USDT | +26.32% | $1,033,938.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +3.72% | +3.72% |
| RAVE/USDT:USDT | below_1h_threshold | +3.31% | +3.30% |
| STORJ/USDT:USDT | below_1h_threshold | +3.11% | +3.10% |
| CNPY/USDT:USDT | below_1h_threshold | +3.10% | +3.10% |
| FF/USDT:USDT | below_1h_threshold | +2.56% | +2.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
