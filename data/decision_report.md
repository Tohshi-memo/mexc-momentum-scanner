# Decision Report

- generated_at: 2026-05-21T10:03:58.426547+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4617**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4617, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.41% | **+1.06%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.03% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.01% | **+1.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.38% | **+1.07%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.34% | **+0.94%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 632件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T10:03:56.377955+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=77600.4
- Funnel: target 766 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +47.77% | $2,991,817.57 |
| EDEN/USDT:USDT | +38.90% | $30,042,915.29 |
| ROAM/USDT:USDT | +38.25% | $2,187,359.02 |
| USELESS/USDT:USDT | +21.52% | $1,851,279.20 |
| SATO/USDT:USDT | +16.54% | $2,837,389.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.33% | +4.32% |
| EDEN/USDT:USDT | below_1h_threshold | +1.66% | +1.66% |
| PROVE/USDT:USDT | below_1h_threshold | +1.45% | +1.45% |
| NIL/USDT:USDT | below_1h_threshold | +1.15% | +1.15% |
| ASTER/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
