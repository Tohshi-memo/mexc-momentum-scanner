# Decision Report

- generated_at: 2026-07-26T15:56:23.218790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9576**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=9576, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.04% | **+1.94%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.46% | **+0.95%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.65% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.94% | **+5.94%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.16% | **+0.64%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.36% | **+0.24%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.18% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.84** / 初期 $100.00 (+354.84%)
- 確定: 3398件 (Win 1078 / Loss 1105 / Flat 1215) / skip 2739件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $454.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1765件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.09** / 初期 $100.00 (+8.09%)
- 確定: 615件 (Win 206 / Loss 238 / Flat 171) / pending 1件 / skip 432件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHIB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.09

## 6. Latest Market Context

- 更新: 2026-07-26T15:56:13.824034+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64747.6
- Funnel: target 898 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +74.93% | $41,796,916.56 |
| DIA/USDT:USDT | +34.23% | $5,558,253.36 |
| ESP/USDT:USDT | +30.77% | $2,001,279.15 |
| BANK/USDT:USDT | +25.91% | $83,406,942.80 |
| KAITO/USDT:USDT | +24.59% | $9,388,597.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +4.48% | +4.39% |
| DIA/USDT:USDT | below_1h_threshold | +4.13% | +4.04% |
| BANK/USDT:USDT | below_1h_threshold | +3.02% | +2.93% |
| BOME/USDT:USDT | below_1h_threshold | +2.78% | +2.69% |
| ONDO/USDT:USDT | below_1h_threshold | +2.67% | +2.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
