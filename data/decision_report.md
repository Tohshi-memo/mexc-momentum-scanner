# Decision Report

- generated_at: 2026-11-15T02:36:25.051314+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18928**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=18928, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.55% | **+0.50%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.01% | **+0.45%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.04% | **+0.76%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.03% | **+0.62%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.75% | **+0.53%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.60% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,728.96** / 初期 $100.00 (+1628.96%)
- 確定: 7332件 (Win 2106 / Loss 2346 / Flat 2880) / skip 8157件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,728.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$428.00** / 初期 $100.00 (+328.00%)
- 確定: 4936件 (Win 1320 / Loss 1080 / Flat 2536) / skip 7403件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0417 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $428.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T02:36:13.851136+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +3.48% price=64768.8
- Funnel: target 1071 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=6, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +13.86% | $2,403,764.82 |
| SOPH/USDT:USDT | +13.58% | $4,406,301.38 |
| PIEVERSE/USDT:USDT | +6.57% | $1,472,613.97 |
| ARIA/USDT:USDT | +6.24% | $2,382,888.11 |
| JCT/USDT:USDT | +4.45% | $5,114,581.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GPS/USDT:USDT | below_relative_strength | +6.72% | +3.24% |
| ZEC/USDT:USDT | below_relative_strength | +5.92% | +2.44% |
| SHELL/USDT:USDT | below_relative_strength | +5.66% | +2.18% |
| VVV/USDT:USDT | below_relative_strength | +5.63% | +2.15% |
| LIT/USDT:USDT | below_relative_strength | +5.30% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
