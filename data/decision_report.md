# Decision Report

- generated_at: 2026-05-27T21:15:08.830182+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4943**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4943, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +3.66% | **+2.38%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.73% | **+2.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.79% | **+1.61%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +3.84% | **+1.35%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.44% | **+0.98%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.29% | **+0.78%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.98% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$96.19** / 初期 $100.00 (-3.81%)
- 確定トレード: 67件 (TP 18 / SL 46 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 820件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T21:15:06.758716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=75132.5
- Funnel: target 771 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +30.39% | $4,601,707.51 |
| RIVER/USDT:USDT | +10.95% | $9,762,650.04 |
| GENIUS/USDT:USDT | +5.98% | $1,231,438.70 |
| GRASS/USDT:USDT | +4.46% | $3,673,053.27 |
| XLM/USDT:USDT | +4.40% | $50,957,080.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +1.27% | +1.42% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.07% | +1.22% |
| NIL/USDT:USDT | below_1h_threshold | +1.01% | +1.16% |
| GRASS/USDT:USDT | below_1h_threshold | +0.56% | +0.70% |
| ORDI/USDT:USDT | below_1h_threshold | +0.52% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
