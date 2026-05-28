# Decision Report

- generated_at: 2026-05-28T00:04:56.138930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4946**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4946, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +4.05% | **+2.43%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.69% | **+2.02%** |
| LIMIT_4PCT | 9/20 | 45.0% | +3.19% | **+1.43%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.77% | **+1.41%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +3.29% | **+1.81%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +4.73% | **+1.66%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.08% | **+1.23%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.46% | **+0.88%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$97.15** / 初期 $100.00 (-2.85%)
- 確定トレード: 68件 (TP 19 / SL 46 / EXP 3)
- 最新: B/USDT:USDT TP_HIT PnL +6.46% 残高後 $97.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 823件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T00:04:54.069202+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=74522.4
- Funnel: target 772 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.15% | $6,344,881.59 |
| NBISSTOCK/USDT:USDT | +14.06% | $1,386,398.46 |
| GENIUS/USDT:USDT | +4.92% | $1,380,785.53 |
| IRENSTOCK/USDT:USDT | +4.77% | $1,007,294.69 |
| RIVER/USDT:USDT | +3.69% | $12,723,112.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +0.84% | +0.70% |
| KLACSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.59% |
| GRASS/USDT:USDT | below_1h_threshold | +0.61% | +0.47% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.46% |
| WLFI/USDT:USDT | below_1h_threshold | +0.51% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
