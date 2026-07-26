# Decision Report

- generated_at: 2026-07-26T04:41:06.177249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9556**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9556, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.23% | **+0.61%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.05% | **+0.04%** |
| LIMIT_BB3S | 2/19 | 10.5% | +0.31% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.99% | **+2.54%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.03% | **+1.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.36% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$468.76** / 初期 $100.00 (+368.76%)
- 確定: 3384件 (Win 1077 / Loss 1097 / Flat 1210) / skip 2733件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $468.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.18** / 初期 $100.00 (+40.18%)
- 確定: 1209件 (Win 337 / Loss 267 / Flat 605) / skip 1758件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1423 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $140.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.63** / 初期 $100.00 (+9.63%)
- 確定: 599件 (Win 205 / Loss 228 / Flat 166) / pending 1件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000601 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $109.63

## 6. Latest Market Context

- 更新: 2026-07-26T04:41:00.810378+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64523.8
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +50.34% | $33,328,884.53 |
| BANK/USDT:USDT | +23.33% | $94,806,524.91 |
| LIGHT/USDT:USDT | +14.82% | $1,409,639.02 |
| SHIB/USDT:USDT | +13.47% | $53,841,817.80 |
| ORDI/USDT:USDT | +12.17% | $4,391,005.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.14% | +3.13% |
| VVV/USDT:USDT | below_1h_threshold | +1.73% | +1.72% |
| EUL/USDT:USDT | below_1h_threshold | +1.62% | +1.62% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.51% | +1.50% |
| ONDO/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
