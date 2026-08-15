# Decision Report

- generated_at: 2026-08-15T06:21:17.168339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11644**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=11644, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.13% | **+1.70%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.32% | **+1.51%** |
| LIMIT_BB3S | 4/17 | 23.5% | +5.45% | **+1.28%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.31% | **+1.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +3.60% | **+1.80%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.89% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.49** / 初期 $100.00 (+540.49%)
- 確定: 4112件 (Win 1287 / Loss 1353 / Flat 1472) / skip 4093件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $640.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.92** / 初期 $100.00 (+54.92%)
- 確定: 1707件 (Win 488 / Loss 409 / Flat 810) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1120 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.60** / 初期 $100.00 (+17.60%)
- 確定: 1588件 (Win 482 / Loss 605 / Flat 501) / pending 3件 / skip 1523件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $117.60

## 6. Latest Market Context

- 更新: 2026-08-15T06:21:08.792417+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63020.5
- Funnel: target 985 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +22.66% | $1,107,919.43 |
| ROBO/USDT:USDT | +20.60% | $5,410,458.54 |
| VELVET/USDT:USDT | +20.00% | $39,962,079.95 |
| ANSEM/USDT:USDT | +19.47% | $1,047,172.41 |
| AIO/USDT:USDT | +18.85% | $1,463,126.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.90% | +1.95% |
| PRL/USDT:USDT | below_1h_threshold | +1.45% | +1.51% |
| ACU/USDT:USDT | below_1h_threshold | +1.27% | +1.32% |
| WLFI/USDT:USDT | below_1h_threshold | +1.09% | +1.14% |
| LDO/USDT:USDT | below_1h_threshold | +0.94% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
