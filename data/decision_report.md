# Decision Report

- generated_at: 2026-10-15T06:46:28.823151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16721**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.28% / filled 20/20。**
- 全期間 MARKET基準: n=16721, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.53% | **+2.53%** |
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |
| LIMIT_2PCT | 18/20 | 90.0% | +2.43% | **+2.19%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.99% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.03% | **-0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,299.52** / 初期 $100.00 (+1199.52%)
- 確定: 6301件 (Win 1847 / Loss 2018 / Flat 2436) / skip 6981件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZKSYNC/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,299.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6459件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000155 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T06:46:14.639227+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=80919.6
- Funnel: target 1085 → liquid 193 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +25.12% | $1,954,759.52 |
| ZKSYNC/USDT:USDT | +19.01% | $4,187,230.22 |
| ZEREBRO/USDT:USDT | +18.09% | $5,332,689.11 |
| NIL/USDT:USDT | +17.64% | $13,932,861.42 |
| SKDD/USDT:USDT | +15.71% | $1,037,415.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.80% | +3.35% |
| DEEP/USDT:USDT | below_1h_threshold | +3.42% | +2.97% |
| SKDD/USDT:USDT | below_1h_threshold | +2.56% | +2.11% |
| OGN/USDT:USDT | below_1h_threshold | +2.33% | +1.87% |
| FLUID/USDT:USDT | below_1h_threshold | +2.31% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
