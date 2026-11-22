# Decision Report

- generated_at: 2026-11-22T17:01:22.101965+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19398**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19398, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_ATR | 8/20 | 40.0% | +0.87% | **+0.35%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.24% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.32%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,833.27** / 初期 $100.00 (+1733.27%)
- 確定: 7508件 (Win 2158 / Loss 2418 / Flat 2932) / skip 8451件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,833.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$461.87** / 初期 $100.00 (+361.87%)
- 確定: 5162件 (Win 1377 / Loss 1114 / Flat 2671) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0546 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $461.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7558件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T17:01:08.307137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=61190.1
- Funnel: target 1086 → liquid 98 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DCTY/USDT:USDT | +5.51% | $1,665,697.63 |
| BEAT/USDT:USDT | +3.34% | $1,613,765.34 |
| NIGHT/USDT:USDT | +2.90% | $2,156,922.11 |
| ENSO/USDT:USDT | +2.61% | $1,158,207.30 |
| ETHFI/USDT:USDT | +1.99% | $1,908,900.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.58% | +1.63% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.55% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.49% | +0.55% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
