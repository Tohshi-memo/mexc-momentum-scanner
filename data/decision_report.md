# Decision Report

- generated_at: 2026-09-25T19:26:31.900513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15539**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15539, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.82% | **-2.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.22% | **+0.37%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.66% | **-0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.06% | **+1.99%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.26% | **+1.79%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.57% | **+1.61%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.59% | **+1.44%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,207.62** / 初期 $100.00 (+1107.62%)
- 確定: 5903件 (Win 1741 / Loss 1891 / Flat 2271) / skip 6197件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEAR/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.56% 残高後 $1,207.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3472件 (Win 953 / Loss 793 / Flat 1726) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0274 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 3件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T19:26:18.859020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=83922.7
- Funnel: target 1067 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +31.02% | $5,840,865.86 |
| BR/USDT:USDT | +15.86% | $8,884,275.72 |
| PHA/USDT:USDT | +13.36% | $14,951,533.05 |
| ONE/USDT:USDT | +12.41% | $9,130,651.01 |
| GRASS/USDT:USDT | +11.88% | $2,249,282.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +4.20% | +4.21% |
| JTO/USDT:USDT | below_1h_threshold | +3.77% | +3.78% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.76% | +3.77% |
| ONE/USDT:USDT | below_1h_threshold | +3.39% | +3.41% |
| TAKE/USDT:USDT | below_1h_threshold | +1.68% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
