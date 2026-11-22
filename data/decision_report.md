# Decision Report

- generated_at: 2026-11-22T14:31:30.933669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19393**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19393, expectancy=+0.02%
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
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,818.78** / 初期 $100.00 (+1718.78%)
- 確定: 7503件 (Win 2156 / Loss 2416 / Flat 2931) / skip 8451件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,818.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.30** / 初期 $100.00 (+360.30%)
- 確定: 5157件 (Win 1375 / Loss 1112 / Flat 2670) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $460.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7553件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000349 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T14:31:12.351664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=60595.7
- Funnel: target 1086 → liquid 104 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +38.12% | $35,971,595.30 |
| CLAUDIA/USDT:USDT | +37.39% | $2,728,719.86 |
| DGAI/USDT:USDT | +25.42% | $1,172,648.23 |
| PIEVERSE/USDT:USDT | +21.96% | $28,783,488.08 |
| NIGHT/USDT:USDT | +14.46% | $2,040,627.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.05% | +2.25% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +1.32% | +1.52% |
| VVV/USDT:USDT | below_1h_threshold | +1.14% | +1.33% |
| BR/USDT:USDT | below_1h_threshold | +0.85% | +1.05% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
