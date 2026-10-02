# Decision Report

- generated_at: 2026-10-02T20:41:25.721667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16020**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16020, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.83% | **+0.82%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.68% | **+0.44%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.46% | **+0.30%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 3/13 | 23.1% | -0.43% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.44% | **+1.46%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.01% | **+0.86%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.57% | **+0.71%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.43% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,335.42** / 初期 $100.00 (+1235.42%)
- 確定: 6125件 (Win 1807 / Loss 1963 / Flat 2355) / skip 6456件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.04% 残高後 $1,335.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5826件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0357 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000152 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T20:41:16.670378+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=84391.0
- Funnel: target 1099 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +14.12% | $1,573,939.76 |
| NMR/USDT:USDT | +7.78% | $1,879,582.07 |
| CT/USDT:USDT | +6.91% | $10,383,868.80 |
| LONGXIA/USDT:USDT | +5.63% | $18,064,464.35 |
| SOXS/USDT:USDT | +2.83% | $30,168,588.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NMR/USDT:USDT | below_relative_strength | +5.10% | +4.95% |
| LSK/USDT:USDT | below_1h_threshold | +3.29% | +3.15% |
| VELVET/USDT:USDT | below_1h_threshold | +3.23% | +3.08% |
| ARK/USDT:USDT | below_1h_threshold | +2.32% | +2.17% |
| CT/USDT:USDT | below_1h_threshold | +2.04% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
