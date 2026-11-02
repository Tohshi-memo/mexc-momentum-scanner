# Decision Report

- generated_at: 2026-11-02T18:16:23.426913+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18031**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=18031, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.01% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.33% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.30% | **+1.11%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.12% | **+0.95%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.67% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,558.61** / 初期 $100.00 (+1458.61%)
- 確定: 6883件 (Win 1997 / Loss 2207 / Flat 2679) / skip 7709件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,558.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$386.61** / 初期 $100.00 (+286.61%)
- 確定: 4471件 (Win 1201 / Loss 994 / Flat 2276) / skip 6971件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0370 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $386.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6189件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T18:16:11.107950+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77192.7
- Funnel: target 1093 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +6.63% | $4,664,961.07 |
| LYN/USDT:USDT | +6.00% | $2,974,430.02 |
| SOXS/USDT:USDT | +4.79% | $17,134,386.98 |
| MAGMA/USDT:USDT | +4.23% | $1,000,240.66 |
| BEAT/USDT:USDT | +3.25% | $6,824,271.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.40% | +2.31% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.36% | +2.27% |
| LYN/USDT:USDT | below_1h_threshold | +2.07% | +1.98% |
| BEAT/USDT:USDT | below_1h_threshold | +1.92% | +1.83% |
| BTW/USDT:USDT | below_1h_threshold | +1.70% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
