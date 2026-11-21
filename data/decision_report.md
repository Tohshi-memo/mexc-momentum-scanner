# Decision Report

- generated_at: 2026-11-21T14:06:17.444651+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19309**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19309, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.29% | **+1.14%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.32% | **+0.66%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.41% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.93% | **+5.93%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.16% | **+2.05%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,659.36** / 初期 $100.00 (+1559.36%)
- 確定: 7452件 (Win 2137 / Loss 2400 / Flat 2915) / skip 8418件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,659.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$455.37** / 初期 $100.00 (+355.37%)
- 確定: 5114件 (Win 1362 / Loss 1094 / Flat 2658) / skip 7606件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0353 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $455.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7470件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T14:06:06.507777+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60545.2
- Funnel: target 1086 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +57.05% | $1,150,131.86 |
| RARE/USDT:USDT | +19.93% | $7,957,351.62 |
| IDOL/USDT:USDT | +19.27% | $1,522,037.79 |
| PIEVERSE/USDT:USDT | +17.35% | $4,026,229.30 |
| VVV/USDT:USDT | +16.90% | $4,698,298.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.80% | +1.77% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.72% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +1.69% | +1.65% |
| RIVER/USDT:USDT | below_1h_threshold | +1.27% | +1.23% |
| BR/USDT:USDT | below_1h_threshold | +1.26% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
