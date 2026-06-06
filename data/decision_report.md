# Decision Report

- generated_at: 2026-06-06T08:10:14.392553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5792**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.46% / filled 20/20。**
- 全期間 MARKET基準: n=5792, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.50% | **+2.50%** |
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.89% | **+0.25%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.28% | **+0.10%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.45% | **+0.09%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +0.12% | **+0.09%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | -0.21% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1340件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T08:10:08.913063+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=61049.9
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +42.78% | $1,043,270.41 |
| CLO/USDT:USDT | +33.66% | $2,312,398.19 |
| ALLO/USDT:USDT | +32.52% | $10,370,604.53 |
| VELVET/USDT:USDT | +31.52% | $2,453,642.23 |
| OPN/USDT:USDT | +25.95% | $20,435,145.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.87% | +2.75% |
| CLO/USDT:USDT | below_1h_threshold | +1.89% | +1.77% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.79% | +1.66% |
| ZEST/USDT:USDT | below_1h_threshold | +1.75% | +1.62% |
| OPN/USDT:USDT | below_1h_threshold | +1.63% | +1.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
