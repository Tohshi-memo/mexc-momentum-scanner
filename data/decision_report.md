# Decision Report

- generated_at: 2026-05-27T04:29:24.041048+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4917**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=4917, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.16% | **+1.04%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.20% | **+0.72%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.01% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.44% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.07** / 初期 $100.00 (+28.07%)
- 確定: 681件 (Win 172 / Loss 218 / Flat 291) / skip 797件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $128.07

## 4. Latest Market Context

- 更新: 2026-05-27T04:29:21.397454+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=75483.7
- Funnel: target 770 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| REQ/USDT:USDT | +22.74% | $1,233,419.83 |
| LUNC/USDT:USDT | +13.00% | $8,675,844.06 |
| GUA/USDT:USDT | +12.84% | $3,503,417.98 |
| PLAY/USDT:USDT | +9.65% | $8,048,255.24 |
| MUSTOCK/USDT:USDT | +6.68% | $33,731,766.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +2.14% | +2.34% |
| GUA/USDT:USDT | below_1h_threshold | +1.98% | +2.18% |
| BEAT/USDT:USDT | below_1h_threshold | +1.31% | +1.51% |
| RIVER/USDT:USDT | below_1h_threshold | +0.81% | +1.02% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
