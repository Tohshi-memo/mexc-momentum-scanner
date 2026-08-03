# Decision Report

- generated_at: 2026-08-03T16:46:27.583322+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10235**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10235, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.14% | **-2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.13% | **+0.34%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.77% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.32% | **+2.32%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.36% | **+2.01%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.93% | **+1.61%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.44% | **+1.37%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.82% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$588.29** / 初期 $100.00 (+488.29%)
- 確定: 3694件 (Win 1172 / Loss 1208 / Flat 1314) / skip 3102件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $588.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2363件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0300 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.47** / 初期 $100.00 (+16.47%)
- 確定: 1018件 (Win 328 / Loss 394 / Flat 296) / pending 6件 / skip 685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000503 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.47

## 6. Latest Market Context

- 更新: 2026-08-03T16:46:18.054547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63755.8
- Funnel: target 929 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.4 >= 65=1, 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +13.00% | $5,538,980.64 |
| PIPPIN/USDT:USDT | +9.17% | $1,454,712.04 |
| HOME/USDT:USDT | +5.11% | $3,394,143.98 |
| RE/USDT:USDT | +4.51% | $1,619,107.95 |
| SNXX/USDT:USDT | +4.43% | $5,958,317.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.86% | +4.71% |
| RE/USDT:USDT | below_1h_threshold | +4.44% | +4.29% |
| 1000RATS/USDT:USDT | below_1h_threshold | +3.86% | +3.71% |
| CAP/USDT:USDT | below_1h_threshold | +2.17% | +2.02% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.89% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
