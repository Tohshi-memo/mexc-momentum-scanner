# Decision Report

- generated_at: 2026-06-06T08:48:46.511320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5795**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=5795, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.36% | **+0.14%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.18% | **+0.06%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.18% | **-0.10%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1343件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T08:48:41.061097+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.60% price=61338.4
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +42.94% | $1,564,164.05 |
| ALLO/USDT:USDT | +40.92% | $11,757,263.59 |
| VELVET/USDT:USDT | +33.81% | $2,515,022.20 |
| CLO/USDT:USDT | +33.47% | $2,439,394.53 |
| OPN/USDT:USDT | +24.48% | $20,764,196.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.95% | +4.35% |
| BEAT/USDT:USDT | below_1h_threshold | +3.87% | +3.27% |
| MEME/USDT:USDT | below_1h_threshold | +3.46% | +2.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.19% | +2.59% |
| SPX/USDT:USDT | below_1h_threshold | +3.18% | +2.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
