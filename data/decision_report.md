# Decision Report

- generated_at: 2026-08-15T09:16:25.642151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11649**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.87% / filled 20/20。**
- 全期間 MARKET基準: n=11649, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.87% | **+2.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.87% | **+2.87%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.19% | **+1.75%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.83% | **+1.56%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.91% | **+1.56%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.04% | **+1.51%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.56% | **+1.10%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4117件 (Win 1288 / Loss 1353 / Flat 1476) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.92** / 初期 $100.00 (+54.92%)
- 確定: 1712件 (Win 488 / Loss 409 / Flat 815) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1317 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $154.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.05** / 初期 $100.00 (+18.05%)
- 確定: 1593件 (Win 484 / Loss 605 / Flat 504) / pending 4件 / skip 1524件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.34% 残高後 $118.05

## 6. Latest Market Context

- 更新: 2026-08-15T09:16:17.053390+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62930.0
- Funnel: target 985 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +26.71% | $4,406,250.75 |
| ROBO/USDT:USDT | +21.61% | $6,753,107.59 |
| VELVET/USDT:USDT | +19.34% | $33,830,207.90 |
| CYS/USDT:USDT | +18.99% | $17,007,914.96 |
| ANSEM/USDT:USDT | +18.62% | $1,238,830.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.94% | +3.91% |
| SYN/USDT:USDT | below_1h_threshold | +1.04% | +1.00% |
| US/USDT:USDT | below_1h_threshold | +0.89% | +0.86% |
| NIL/USDT:USDT | below_1h_threshold | +0.77% | +0.73% |
| ON/USDT:USDT | below_1h_threshold | +0.74% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
