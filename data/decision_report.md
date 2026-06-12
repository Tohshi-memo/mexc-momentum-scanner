# Decision Report

- generated_at: 2026-06-12T15:26:12.306533+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6518**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=6518, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.72% | **+1.11%** |
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.25% | **+0.12%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.34** / 初期 $100.00 (+66.34%)
- 確定: 1391件 (Win 383 / Loss 452 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $166.34

## 4. Latest Market Context

- 更新: 2026-06-12T15:26:09.612581+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=64274.9
- Funnel: target 774 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +88.81% | $61,680,439.95 |
| NAORIS/USDT:USDT | +41.75% | $6,748,141.11 |
| XPL/USDT:USDT | +40.40% | $15,872,980.93 |
| SKYAI/USDT:USDT | +38.51% | $17,703,996.03 |
| AIN/USDT:USDT | +36.72% | $1,442,932.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.96% | +1.48% |
| JUP/USDT:USDT | below_1h_threshold | +1.96% | +1.48% |
| H/USDT:USDT | below_1h_threshold | +1.89% | +1.41% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.74% | +1.27% |
| SOXL/USDT:USDT | below_1h_threshold | +1.72% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
