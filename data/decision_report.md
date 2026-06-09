# Decision Report

- generated_at: 2026-06-09T01:28:35.203896+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6109**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=6109, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.49% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.72** / 初期 $100.00 (+52.72%)
- 確定: 1149件 (Win 283 / Loss 352 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.72

## 4. Latest Market Context

- 更新: 2026-06-09T01:28:32.555570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=62809.3
- Funnel: target 777 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +34.01% | $23,723,765.75 |
| 4/USDT:USDT | +29.55% | $1,521,153.47 |
| MOVE/USDT:USDT | +29.15% | $2,855,046.66 |
| PIPPIN/USDT:USDT | +11.86% | $31,428,569.21 |
| FOLKS/USDT:USDT | +7.94% | $1,411,416.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +3.20% | +2.75% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.04% | +2.59% |
| BLESS/USDT:USDT | below_1h_threshold | +2.92% | +2.47% |
| CHZ/USDT:USDT | below_1h_threshold | +1.93% | +1.47% |
| SIREN/USDT:USDT | below_1h_threshold | +1.69% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
