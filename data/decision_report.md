# Decision Report

- generated_at: 2026-09-17T22:11:26.109843+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14844**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14844, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.55% | **-0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.82% | **+0.85%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.65% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.48% | **+1.86%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.54% | **+1.78%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.43% | **+1.15%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.10% | **+0.99%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5603件 (Win 1679 / Loss 1814 / Flat 2110) / skip 5802件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.42** / 初期 $100.00 (+141.42%)
- 確定: 3138件 (Win 873 / Loss 748 / Flat 1517) / skip 5117件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0835 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $241.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3360件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000312 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T22:11:17.506774+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76350.2
- Funnel: target 1052 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +48.45% | $2,885,502.34 |
| ONE/USDT:USDT | +27.08% | $35,900,108.72 |
| COTI/USDT:USDT | +27.07% | $4,591,267.64 |
| CROSS/USDT:USDT | +21.30% | $1,322,226.08 |
| UNI/USDT:USDT | +8.04% | $56,079,021.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +1.82% | +1.85% |
| CNPY/USDT:USDT | below_1h_threshold | +1.62% | +1.65% |
| SAGA/USDT:USDT | below_1h_threshold | +1.43% | +1.47% |
| UAI/USDT:USDT | below_1h_threshold | +0.79% | +0.82% |
| SOXL/USDT:USDT | below_1h_threshold | +0.31% | +0.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
