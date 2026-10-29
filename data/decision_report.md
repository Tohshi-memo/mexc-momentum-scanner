# Decision Report

- generated_at: 2026-10-29T02:46:41.574422+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17750**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.62% / filled 20/20。**
- 全期間 MARKET基準: n=17750, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_BB3S | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.56% | **+0.51%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.21% | **-0.05%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.12% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,561.10** / 初期 $100.00 (+1461.10%)
- 確定: 6794件 (Win 1973 / Loss 2173 / Flat 2648) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,561.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.75** / 初期 $100.00 (+258.75%)
- 確定: 4271件 (Win 1156 / Loss 971 / Flat 2144) / skip 6890件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0126 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $358.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5911件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000338 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T02:46:28.144127+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=79724.1
- Funnel: target 1083 → liquid 173 → pre 50 → checked 49 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +63.13% | $2,054,422.64 |
| BULLA/USDT:USDT | +13.22% | $3,031,195.21 |
| INIT/USDT:USDT | +12.71% | $2,140,596.52 |
| AKE/USDT:USDT | +7.73% | $6,887,911.52 |
| ORCLSTOCK/USDT:USDT | +7.50% | $5,139,622.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKDD/USDT:USDT | below_1h_threshold | +3.01% | +3.32% |
| UNITREE/USDT:USDT | below_1h_threshold | +2.90% | +3.21% |
| SOXS/USDT:USDT | below_1h_threshold | +2.58% | +2.89% |
| AKE/USDT:USDT | below_1h_threshold | +1.45% | +1.76% |
| BTW/USDT:USDT | below_1h_threshold | +1.29% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
