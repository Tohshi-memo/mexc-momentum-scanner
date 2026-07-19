# Decision Report

- generated_at: 2026-07-19T21:41:08.318382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9068**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.61% / filled 20/20。**
- 全期間 MARKET基準: n=9068, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.43%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.45% | **-0.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.14% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.72** / 初期 $100.00 (+299.72%)
- 確定: 3130件 (Win 983 / Loss 1000 / Flat 1147) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $399.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.64** / 初期 $100.00 (+25.64%)
- 確定: 1029件 (Win 265 / Loss 218 / Flat 546) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.87** / 初期 $100.00 (+0.87%)
- 確定: 268件 (Win 93 / Loss 131 / Flat 44) / pending 2件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.87

## 6. Latest Market Context

- 更新: 2026-07-19T21:41:01.906010+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64377.0
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +45.96% | $74,980,746.09 |
| PROM/USDT:USDT | +16.19% | $1,658,298.82 |
| B/USDT:USDT | +15.74% | $39,576,673.17 |
| PUMPFUN/USDT:USDT | +13.78% | $7,859,734.48 |
| DEXE/USDT:USDT | +8.04% | $1,541,497.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.87% | +3.09% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.75% | +2.97% |
| B/USDT:USDT | below_1h_threshold | +1.54% | +1.76% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.12% | +1.34% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.43% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
