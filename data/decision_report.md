# Decision Report

- generated_at: 2026-10-12T15:31:20.024664+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16603**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16603, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.37% | **+0.16%** |
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |
| LIMIT_5PCT | 5/20 | 25.0% | -1.03% | **-0.26%** |
| LIMIT_6PCT | 3/20 | 15.0% | -2.04% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.50% | **+1.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.51% | **+1.06%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.75** / 初期 $100.00 (+1191.75%)
- 確定: 6292件 (Win 1845 / Loss 2016 / Flat 2431) / skip 6872件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,291.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.12** / 初期 $100.00 (+172.12%)
- 確定: 3639件 (Win 1010 / Loss 855 / Flat 1774) / skip 6375件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RSR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $272.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4761件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-12T15:31:08.021484+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=82618.1
- Funnel: target 1089 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RSR/USDT:USDT | +48.50% | $13,145,191.64 |
| W/USDT:USDT | +35.70% | $46,089,382.56 |
| BATON/USDT:USDT | +11.32% | $4,088,616.02 |
| PYTH/USDT:USDT | +10.35% | $9,890,340.04 |
| SOXS/USDT:USDT | +9.98% | $29,755,429.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.83% | +1.74% |
| CKB/USDT:USDT | below_1h_threshold | +1.60% | +1.51% |
| PLUME/USDT:USDT | below_1h_threshold | +1.59% | +1.50% |
| SOXS/USDT:USDT | below_1h_threshold | +1.20% | +1.11% |
| RSR/USDT:USDT | below_1h_threshold | +0.87% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
