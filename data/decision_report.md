# Decision Report

- generated_at: 2026-06-07T21:07:04.067144+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6000**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=6000, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.32% | **+0.32%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.62% | **+0.21%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.69% | **+5.69%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.46% | **+1.10%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.72** / 初期 $100.00 (+52.72%)
- 確定: 1117件 (Win 272 / Loss 336 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $152.72

## 4. Latest Market Context

- 更新: 2026-06-07T21:07:01.298230+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=61743.0
- Funnel: target 768 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +23.03% | $3,597,692.52 |
| BTW/USDT:USDT | +19.35% | $13,580,663.32 |
| BEAT/USDT:USDT | +19.32% | $62,315,703.51 |
| EPIC/USDT:USDT | +16.30% | $1,302,796.89 |
| BLESS/USDT:USDT | +9.63% | $7,675,517.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.82% | +2.98% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.22% | +1.38% |
| EPIC/USDT:USDT | below_1h_threshold | +0.86% | +1.02% |
| COPSTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.66% |
| BLUAI/USDT:USDT | below_1h_threshold | +0.45% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
