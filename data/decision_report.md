# Decision Report

- generated_at: 2026-06-04T16:18:18.094242+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5643**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5643, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/13 | 53.8% | +2.72% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.88% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 97件 (TP 30 / SL 64 / EXP 3)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1197件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T16:18:15.246882+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=63696.0
- Funnel: target 772 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +3.09% | $2,819,799.45 |
| USELESS/USDT:USDT | +2.18% | $2,460,983.03 |
| NIL/USDT:USDT | +1.72% | $1,220,828.42 |
| NEAR/USDT:USDT | +1.63% | $203,426,710.03 |
| ARMSTOCK/USDT:USDT | +1.52% | $1,525,481.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.09% | +3.36% |
| USELESS/USDT:USDT | below_1h_threshold | +2.18% | +2.45% |
| NEAR/USDT:USDT | below_1h_threshold | +1.63% | +1.89% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.79% |
| NIL/USDT:USDT | below_1h_threshold | +1.48% | +1.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
