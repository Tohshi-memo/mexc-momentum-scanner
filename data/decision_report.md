# Decision Report

- generated_at: 2026-06-06T08:43:16.832264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5794**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.86% / filled 20/20。**
- 全期間 MARKET基準: n=5794, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.61% | **+0.21%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.18% | **+0.06%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.35% | **-0.21%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.46% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1342件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T08:43:14.490018+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=61349.1
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +42.43% | $1,505,779.92 |
| ALLO/USDT:USDT | +38.81% | $11,434,948.76 |
| CLO/USDT:USDT | +33.29% | $2,430,148.51 |
| VELVET/USDT:USDT | +32.68% | $2,494,301.98 |
| OPN/USDT:USDT | +24.92% | $20,740,939.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.49% | +4.87% |
| SIREN/USDT:USDT | below_1h_threshold | +4.83% | +4.22% |
| BEAT/USDT:USDT | below_1h_threshold | +3.60% | +2.99% |
| BTW/USDT:USDT | below_1h_threshold | +3.49% | +2.87% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.38% | +2.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
