# Decision Report

- generated_at: 2026-09-24T17:21:24.789914+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15484**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15484, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.30%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.15% | **+0.10%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.21% | **-0.16%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.39% | **-0.18%** |
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +2.20% | **+1.71%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.13% | **+0.74%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6146件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.04** / 初期 $100.00 (+154.04%)
- 確定: 3431件 (Win 947 / Loss 791 / Flat 1693) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0242 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $254.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3799件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T17:21:13.506198+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=84314.3
- Funnel: target 1069 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +3.97% | $2,060,766.32 |
| TRB/USDT:USDT | +3.97% | $1,079,135.56 |
| SOXL/USDT:USDT | +3.63% | $37,739,830.82 |
| EGLD/USDT:USDT | +3.05% | $2,164,179.43 |
| NIL/USDT:USDT | +2.88% | $26,627,164.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.52% | +4.68% |
| MVLL/USDT:USDT | below_1h_threshold | +2.87% | +3.03% |
| MUU/USDT:USDT | below_1h_threshold | +2.73% | +2.89% |
| TQQQ/USDT:USDT | below_1h_threshold | +2.43% | +2.59% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.37% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
