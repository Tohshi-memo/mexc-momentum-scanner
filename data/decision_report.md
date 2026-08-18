# Decision Report

- generated_at: 2026-08-18T03:01:27.573894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11876**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.18% / filled 20/20。**
- 全期間 MARKET基準: n=11876, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_3PCT | 9/20 | 45.0% | +3.34% | **+1.50%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.32% | **+1.39%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.27% | **+1.28%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.78% | **+1.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.23% | **+1.00%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.01% | **+0.55%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.38% | **+0.28%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4250件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3468件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0725 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.67** / 初期 $100.00 (+17.67%)
- 確定: 1687件 (Win 505 / Loss 641 / Flat 541) / pending 5件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STAR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.67

## 6. Latest Market Context

- 更新: 2026-08-18T03:01:15.984851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64088.5
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +15.59% | $1,868,427.37 |
| CYS/USDT:USDT | +8.87% | $17,880,330.18 |
| SOXS/USDT:USDT | +7.50% | $5,299,622.83 |
| H/USDT:USDT | +7.24% | $6,458,431.03 |
| TUT/USDT:USDT | +6.00% | $29,500,610.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.25% | +2.22% |
| CYS/USDT:USDT | below_1h_threshold | +0.91% | +0.88% |
| APR/USDT:USDT | below_1h_threshold | +0.37% | +0.35% |
| HEMI/USDT:USDT | below_1h_threshold | +0.32% | +0.29% |
| ZEC/USDT:USDT | below_1h_threshold | +0.20% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
