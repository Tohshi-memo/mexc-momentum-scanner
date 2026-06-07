# Decision Report

- generated_at: 2026-06-07T23:02:22.482394+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=6005, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/16 | 18.8% | +2.45% | **+0.46%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.03% | **+0.26%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.46** / 初期 $100.00 (+53.46%)
- 確定: 1122件 (Win 274 / Loss 339 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $153.46

## 4. Latest Market Context

- 更新: 2026-06-07T23:02:19.994222+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62990.4
- Funnel: target 769 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +33.50% | $14,825,556.12 |
| BANK/USDT:USDT | +28.52% | $4,040,699.68 |
| BEAT/USDT:USDT | +23.28% | $76,989,012.47 |
| PIPPIN/USDT:USDT | +21.01% | $4,298,942.75 |
| BLESS/USDT:USDT | +15.95% | $8,415,838.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +0.67% | +0.42% |
| GUA/USDT:USDT | below_1h_threshold | +0.62% | +0.38% |
| ZEC/USDT:USDT | below_1h_threshold | +0.54% | +0.29% |
| SAHARA/USDT:USDT | below_1h_threshold | +0.45% | +0.21% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.45% | +0.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
