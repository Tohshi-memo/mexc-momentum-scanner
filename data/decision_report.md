# Decision Report

- generated_at: 2026-05-28T15:39:50.550463+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4971**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=4971, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.56% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +1.11% | **+0.99%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.42** / 初期 $100.00 (+27.42%)
- 確定: 706件 (Win 173 / Loss 221 / Flat 312) / skip 826件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $127.42

## 4. Latest Market Context

- 更新: 2026-05-28T15:39:48.405157+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=72866.7
- Funnel: target 776 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +35.20% | $12,046,718.81 |
| ONDSSTOCK/USDT:USDT | +28.17% | $1,214,325.32 |
| XLM/USDT:USDT | +22.61% | $259,471,386.66 |
| ESPORTS/USDT:USDT | +22.27% | $5,407,351.55 |
| ALLO/USDT:USDT | +19.75% | $1,072,667.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +4.88% | +5.06% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.61% | +2.79% |
| ALLO/USDT:USDT | below_1h_threshold | +2.05% | +2.23% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +2.09% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
