# Decision Report

- generated_at: 2026-08-04T04:36:20.641222+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10265**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=10265, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_4PCT | 8/20 | 40.0% | +1.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.44% | **-0.44%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | -0.62% | **-0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$584.79** / 初期 $100.00 (+484.79%)
- 確定: 3723件 (Win 1179 / Loss 1219 / Flat 1325) / skip 3103件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $584.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2392件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0463 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.95** / 初期 $100.00 (+16.95%)
- 確定: 1036件 (Win 334 / Loss 401 / Flat 301) / pending 6件 / skip 700件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.95

## 6. Latest Market Context

- 更新: 2026-08-04T04:36:11.339104+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63845.8
- Funnel: target 929 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +22.57% | $19,546,773.80 |
| HOME/USDT:USDT | +19.19% | $4,693,068.92 |
| ON/USDT:USDT | +16.35% | $2,965,794.37 |
| PLTRSTOCK/USDT:USDT | +15.60% | $4,000,366.78 |
| NIL/USDT:USDT | +13.70% | $1,797,316.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +3.53% | +3.41% |
| NIL/USDT:USDT | below_1h_threshold | +2.60% | +2.48% |
| VANRY/USDT:USDT | below_1h_threshold | +2.56% | +2.45% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.29% |
| COTI/USDT:USDT | below_1h_threshold | +1.98% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
