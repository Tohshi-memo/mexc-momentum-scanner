# Decision Report

- generated_at: 2026-11-15T10:06:21.073016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18954**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18954, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +3.69% | **+0.37%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.34% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +6.78% | **+6.78%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.71** / 初期 $100.00 (+1611.71%)
- 確定: 7335件 (Win 2106 / Loss 2348 / Flat 2881) / skip 8180件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,711.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$428.60** / 初期 $100.00 (+328.60%)
- 確定: 4962件 (Win 1327 / Loss 1081 / Flat 2554) / skip 7403件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0246 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KAVA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $428.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7113件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000110 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T10:06:07.569864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=65443.0
- Funnel: target 1066 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +31.75% | $4,853,405.73 |
| JCT/USDT:USDT | +10.69% | $4,462,706.55 |
| ARIA/USDT:USDT | +10.26% | $2,514,482.56 |
| PIEVERSE/USDT:USDT | +9.68% | $1,897,422.27 |
| VVV/USDT:USDT | +9.50% | $3,762,142.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.48% | +3.28% |
| SNXX/USDT:USDT | below_1h_threshold | +1.03% | +0.83% |
| HYPE/USDT:USDT | below_1h_threshold | +0.83% | +0.64% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.58% |
| FET/USDT:USDT | below_1h_threshold | +0.68% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
