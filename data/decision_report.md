# Decision Report

- generated_at: 2026-06-05T08:21:43.891768+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5703**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=5703, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.97% | **+0.74%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.16% | **+0.10%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.54% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1009件 (Win 239 / Loss 312 / Flat 458) / skip 1255件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T08:21:41.102482+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.75% price=62604.9
- Funnel: target 772 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +65.92% | $20,987,576.04 |
| OPN/USDT:USDT | +35.96% | $37,450,829.89 |
| MEME/USDT:USDT | +13.92% | $2,274,411.76 |
| BEAT/USDT:USDT | +11.82% | $26,043,769.16 |
| AAOISTOCK/USDT:USDT | +9.17% | $1,610,631.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEME/USDT:USDT | below_1h_threshold | +1.58% | +2.33% |
| EPIC/USDT:USDT | below_1h_threshold | +1.17% | +1.91% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.88% |
| AIA/USDT:USDT | below_1h_threshold | +0.88% | +1.63% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
