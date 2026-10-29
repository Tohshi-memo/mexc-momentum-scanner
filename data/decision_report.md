# Decision Report

- generated_at: 2026-10-29T18:01:26.874128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17798**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.03% / filled 20/20。**
- 全期間 MARKET基準: n=17798, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_BB3S | 4/10 | 40.0% | +1.39% | **+0.55%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.82% | **+0.54%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +0.70% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7555件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.43** / 初期 $100.00 (+263.43%)
- 確定: 4319件 (Win 1165 / Loss 979 / Flat 2175) / skip 6890件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0001 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PARTI/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $363.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5959件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T18:01:16.799121+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80840.0
- Funnel: target 1086 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +64.00% | $1,622,903.48 |
| BLESS/USDT:USDT | +15.10% | $10,003,983.29 |
| BULLA/USDT:USDT | +7.49% | $1,533,863.35 |
| UAI/USDT:USDT | +4.84% | $2,740,325.52 |
| SOXS/USDT:USDT | +3.85% | $78,047,605.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.30% | +2.32% |
| SOXS/USDT:USDT | below_1h_threshold | +2.10% | +2.12% |
| JCT/USDT:USDT | below_1h_threshold | +1.37% | +1.40% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.27% | +1.29% |
| AIN/USDT:USDT | below_1h_threshold | +0.95% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
