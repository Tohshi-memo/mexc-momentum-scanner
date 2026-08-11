# Decision Report

- generated_at: 2026-08-11T20:26:21.634716+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11294**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=11294, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.98% | **+0.83%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.36% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.66% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +3.34% | **+2.34%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.89% | **+1.04%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 179件 (TP 69 / SL 105 / EXP 5)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3938件 (Win 1230 / Loss 1285 / Flat 1423) / skip 3917件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.64** / 初期 $100.00 (+43.64%)
- 確定: 1548件 (Win 434 / Loss 363 / Flat 751) / skip 3157件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0415 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1437件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T20:26:14.097058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63592.0
- Funnel: target 967 → liquid 194 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +14.83% | $2,454,755.26 |
| HOLO/USDT:USDT | +14.43% | $1,165,761.48 |
| CRWVSTOCK/USDT:USDT | +9.71% | $2,305,584.73 |
| SMCISTOCK/USDT:USDT | +8.91% | $1,842,399.06 |
| CAP/USDT:USDT | +8.73% | $7,343,255.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +3.97% | +3.84% |
| BEAT/USDT:USDT | below_1h_threshold | +3.33% | +3.19% |
| HOLO/USDT:USDT | below_1h_threshold | +3.20% | +3.06% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.69% |
| MUU/USDT:USDT | below_1h_threshold | +2.48% | +2.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
