# Decision Report

- generated_at: 2026-11-22T13:01:15.940664+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19387**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19387, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.84% | **+2.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.82% | **+1.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.13% | **+1.60%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.38% | **+1.19%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,809.96** / 初期 $100.00 (+1709.96%)
- 確定: 7497件 (Win 2154 / Loss 2413 / Flat 2930) / skip 8451件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,809.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$459.59** / 初期 $100.00 (+359.59%)
- 確定: 5151件 (Win 1373 / Loss 1109 / Flat 2669) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0658 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $459.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7547件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T13:01:05.483212+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=60865.5
- Funnel: target 1086 → liquid 105 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +42.39% | $2,694,594.67 |
| BLESS/USDT:USDT | +24.38% | $31,854,403.21 |
| DCTY/USDT:USDT | +18.45% | $1,780,983.20 |
| VELVET/USDT:USDT | +15.23% | $1,253,174.97 |
| BTW/USDT:USDT | +15.11% | $4,611,041.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.56% | +1.49% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.56% | +0.50% |
| KORU/USDT:USDT | below_1h_threshold | +0.50% | +0.43% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.30% | +0.23% |
| JUP/USDT:USDT | below_1h_threshold | +0.27% | +0.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
