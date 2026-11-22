# Decision Report

- generated_at: 2026-11-22T15:06:22.584420+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19394**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19394, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.26% | **+2.12%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.40% | **+2.04%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,835.19** / 初期 $100.00 (+1735.19%)
- 確定: 7504件 (Win 2157 / Loss 2416 / Flat 2931) / skip 8451件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $1,835.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$462.70** / 初期 $100.00 (+362.70%)
- 確定: 5158件 (Win 1376 / Loss 1112 / Flat 2670) / skip 7647件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0486 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $462.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7555件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T15:06:11.174058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=60994.0
- Funnel: target 1086 → liquid 102 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +45.79% | $35,413,003.07 |
| CLAUDIA/USDT:USDT | +41.72% | $2,670,839.68 |
| DGAI/USDT:USDT | +27.78% | $1,259,004.74 |
| PIEVERSE/USDT:USDT | +25.27% | $29,731,797.44 |
| VELVET/USDT:USDT | +15.30% | $1,339,323.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.99% | +3.84% |
| DCTY/USDT:USDT | below_1h_threshold | +2.05% | +1.90% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.88% | +0.73% |
| VVV/USDT:USDT | below_1h_threshold | +0.84% | +0.69% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.76% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
