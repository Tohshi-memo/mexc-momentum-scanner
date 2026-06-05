# Decision Report

- generated_at: 2026-06-05T07:53:43.701436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5701**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=5701, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.39% | **+0.42%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.52% | **+1.06%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1009件 (Win 239 / Loss 312 / Flat 458) / skip 1253件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T07:53:40.911669+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.47% price=62827.1
- Funnel: target 772 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1, 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +70.17% | $20,605,769.82 |
| OPN/USDT:USDT | +35.06% | $37,249,317.87 |
| BEAT/USDT:USDT | +13.78% | $26,792,913.33 |
| HOME/USDT:USDT | +12.53% | $8,569,429.41 |
| MEME/USDT:USDT | +12.30% | $2,248,882.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEME/USDT:USDT | below_relative_strength | +5.95% | +4.48% |
| LIT/USDT:USDT | below_relative_strength | +5.33% | +3.86% |
| AIA/USDT:USDT | below_1h_threshold | +4.14% | +2.67% |
| MONAD/USDT:USDT | below_1h_threshold | +3.99% | +2.52% |
| KAS/USDT:USDT | below_1h_threshold | +3.56% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
