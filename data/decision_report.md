# Decision Report

- generated_at: 2026-11-02T23:01:33.324037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18040**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18040, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.54% | **-0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.66% | **+1.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.13% | **+1.17%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.12%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.12% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$121.86** / 初期 $100.00 (+21.86%)
- 確定トレード: 259件 (TP 96 / SL 155 / EXP 8)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.86
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,560.16** / 初期 $100.00 (+1460.16%)
- 確定: 6892件 (Win 1998 / Loss 2210 / Flat 2684) / skip 7709件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,560.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$380.43** / 初期 $100.00 (+280.43%)
- 確定: 4479件 (Win 1203 / Loss 999 / Flat 2277) / skip 6972件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0032 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $380.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6202件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T23:01:23.998313+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=76806.8
- Funnel: target 1093 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +28.04% | $17,270,826.08 |
| Q/USDT:USDT | +11.36% | $5,671,721.03 |
| EVAA/USDT:USDT | +9.86% | $6,057,171.76 |
| SOXS/USDT:USDT | +9.44% | $23,803,355.08 |
| JCT/USDT:USDT | +7.27% | $2,116,860.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQQQ/USDT:USDT | below_1h_threshold | +0.49% | +0.63% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.17% | +0.31% |
| AIN/USDT:USDT | below_1h_threshold | +0.16% | +0.31% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.11% | +0.25% |
| ZINC/USDT:USDT | below_1h_threshold | +0.04% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
