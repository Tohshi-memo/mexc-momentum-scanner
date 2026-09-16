# Decision Report

- generated_at: 2026-09-16T04:01:26.158503+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14630**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.86% / filled 20/20。**
- 全期間 MARKET基準: n=14630, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.86% | **+2.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.86% | **+2.86%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.97% | **+2.53%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.15% | **+1.89%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.58% | **+1.81%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.59% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.17% | **+0.10%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.63% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5674件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4987件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.36** / 初期 $100.00 (+25.36%)
- 確定: 2921件 (Win 869 / Loss 1139 / Flat 913) / pending 3件 / skip 3177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000326 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.36

## 6. Latest Market Context

- 更新: 2026-09-16T04:01:13.660005+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=75798.5
- Funnel: target 1064 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +29.77% | $2,250,924.80 |
| LSK/USDT:USDT | +18.88% | $16,619,263.53 |
| ON/USDT:USDT | +15.58% | $3,109,142.37 |
| LONGXIA/USDT:USDT | +14.27% | $1,831,286.55 |
| USELESS/USDT:USDT | +9.52% | $4,982,010.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.50% | +1.48% |
| KORU/USDT:USDT | below_1h_threshold | +1.48% | +1.46% |
| SNXX/USDT:USDT | below_1h_threshold | +0.98% | +0.96% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.81% | +0.79% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
