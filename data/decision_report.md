# Decision Report

- generated_at: 2026-08-17T12:01:26.063418+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11822**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=11822, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.89% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.43% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.61% | **+0.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.79** / 初期 $100.00 (+517.79%)
- 確定: 4185件 (Win 1292 / Loss 1364 / Flat 1529) / skip 4198件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $617.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3415件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0006 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.75** / 初期 $100.00 (+17.75%)
- 確定: 1675件 (Win 503 / Loss 638 / Flat 534) / pending 2件 / skip 1617件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.75

## 6. Latest Market Context

- 更新: 2026-08-17T12:01:16.064580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63595.0
- Funnel: target 992 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +133.10% | $2,083,232.20 |
| GPS/USDT:USDT | +59.57% | $13,834,285.14 |
| ACE/USDT:USDT | +37.11% | $24,942,712.46 |
| PORTAL/USDT:USDT | +23.67% | $18,468,657.77 |
| AEON1/USDT:USDT | +16.42% | $1,202,672.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +0.51% | +0.52% |
| ACE/USDT:USDT | below_1h_threshold | +0.40% | +0.40% |
| AKE/USDT:USDT | below_1h_threshold | +0.38% | +0.38% |
| AEON1/USDT:USDT | below_1h_threshold | +0.35% | +0.36% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.22% | +0.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
