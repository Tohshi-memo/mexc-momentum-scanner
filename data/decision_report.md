# Decision Report

- generated_at: 2026-08-11T22:36:28.111184+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11304**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=11304, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.32% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.25% | **+1.12%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.65% | **+0.82%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.36% | **+0.81%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3926件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.74** / 初期 $100.00 (+43.74%)
- 確定: 1558件 (Win 435 / Loss 363 / Flat 760) / skip 3157件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0022 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSPSTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T22:36:18.360022+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63696.7
- Funnel: target 967 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +43.80% | $1,187,108.05 |
| LSK/USDT:USDT | +20.87% | $2,380,284.60 |
| HOLO/USDT:USDT | +16.46% | $2,392,850.22 |
| CRWVSTOCK/USDT:USDT | +15.67% | $3,356,215.62 |
| BMT/USDT:USDT | +14.34% | $2,539,822.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.03% | +1.94% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +1.77% |
| 4/USDT:USDT | below_1h_threshold | +1.49% | +1.40% |
| BTW/USDT:USDT | below_1h_threshold | +1.49% | +1.40% |
| HOME/USDT:USDT | below_1h_threshold | +1.47% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
