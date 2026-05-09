# Decision Report

- generated_at: 2026-05-09T23:13:23.966697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3922**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=3922, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.41% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.38%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.06% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 287件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-09T23:13:21.083746+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80691.5
- Funnel: target 769 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +23.87% | $7,475,992.61 |
| SATO/USDT:USDT | +19.82% | $5,247,667.56 |
| BILL/USDT:USDT | +16.49% | $38,371,036.60 |
| MITO/USDT:USDT | +15.50% | $3,159,930.01 |
| JASMY/USDT:USDT | +15.05% | $12,356,423.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.82% | +3.87% |
| INX/USDT:USDT | below_1h_threshold | +1.36% | +1.40% |
| JASMY/USDT:USDT | below_1h_threshold | +1.21% | +1.26% |
| FHE/USDT:USDT | below_1h_threshold | +1.06% | +1.11% |
| UB/USDT:USDT | below_1h_threshold | +0.81% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
