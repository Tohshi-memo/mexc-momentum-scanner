# Decision Report

- generated_at: 2026-07-31T02:01:19.243777+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9948**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9948, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.34% | **+0.34%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.75% | **+2.75%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.37% | **+2.36%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.27% | **+1.48%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.44% | **+1.34%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.36% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$531.39** / 初期 $100.00 (+431.39%)
- 確定: 3539件 (Win 1126 / Loss 1152 / Flat 1261) / skip 2970件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $531.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.09** / 初期 $100.00 (+38.09%)
- 確定: 1245件 (Win 346 / Loss 283 / Flat 616) / skip 2114件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2162 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $138.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 619件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000682 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T02:01:11.906650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64548.2
- Funnel: target 920 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +28.03% | $3,700,056.49 |
| MMT/USDT:USDT | +23.55% | $9,250,895.61 |
| ZHIPUSTOCK/USDT:USDT | +19.85% | $5,430,723.87 |
| SNXX/USDT:USDT | +18.40% | $11,272,515.78 |
| AMZU/USDT:USDT | +16.73% | $1,916,086.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.28% |
| TESLA/USDT:USDT | below_1h_threshold | +1.23% | +1.21% |
| MMT/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| AMZU/USDT:USDT | below_1h_threshold | +0.40% | +0.38% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.33% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
