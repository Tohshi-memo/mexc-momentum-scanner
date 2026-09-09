# Decision Report

- generated_at: 2026-09-09T12:56:36.080030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14068**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14068, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.88% | **+0.85%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.70% | **+0.52%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5316件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.33** / 初期 $100.00 (+90.33%)
- 確定: 2664件 (Win 731 / Loss 627 / Flat 1306) / skip 4815件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0170 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $190.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2922件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T12:56:26.644885+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=79556.0
- Funnel: target 1064 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +71.11% | $1,742,285.71 |
| IOST/USDT:USDT | +37.65% | $7,188,531.62 |
| OL/USDT:USDT | +23.20% | $2,366,799.52 |
| RAY/USDT:USDT | +19.57% | $6,121,609.15 |
| BR/USDT:USDT | +19.30% | $1,868,273.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_relative_strength | +5.26% | +4.91% |
| MARSCOIN/USDT:USDT | below_relative_strength | +5.04% | +4.69% |
| UAI/USDT:USDT | below_1h_threshold | +4.74% | +4.39% |
| 4/USDT:USDT | below_1h_threshold | +3.14% | +2.79% |
| IOST/USDT:USDT | below_1h_threshold | +2.53% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
