# Decision Report

- generated_at: 2026-11-23T05:41:22.563128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19421**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.95% / filled 20/20。**
- 全期間 MARKET基準: n=19421, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.37% | **+0.89%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.24% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.19% | **+0.66%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.01% | **+0.65%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,846.15** / 初期 $100.00 (+1746.15%)
- 確定: 7521件 (Win 2161 / Loss 2423 / Flat 2937) / skip 8461件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $1,846.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.38** / 初期 $100.00 (+365.38%)
- 確定: 5183件 (Win 1382 / Loss 1117 / Flat 2684) / skip 7649件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0796 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $465.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7582件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T05:41:09.225130+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=61627.8
- Funnel: target 1086 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +56.30% | $1,608,056.40 |
| ELSA/USDT:USDT | +18.42% | $1,881,728.62 |
| ARIA/USDT:USDT | +16.09% | $1,733,804.94 |
| UNITREE/USDT:USDT | +13.41% | $1,106,250.26 |
| EVAA/USDT:USDT | +11.45% | $50,007,528.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.86% | +4.19% |
| JUP/USDT:USDT | below_1h_threshold | +3.67% | +3.00% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.21% | +2.54% |
| ARIA/USDT:USDT | below_1h_threshold | +3.09% | +2.42% |
| QNT/USDT:USDT | below_1h_threshold | +2.56% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
