# Decision Report

- generated_at: 2026-10-04T18:36:27.887056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16122**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=16122, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.73% | **+2.60%** |
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_10PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.73% | **+1.04%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.31% | **+0.79%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,313.90** / 初期 $100.00 (+1213.90%)
- 確定: 6181件 (Win 1821 / Loss 1983 / Flat 2377) / skip 6502件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,313.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3609件 (Win 1005 / Loss 845 / Flat 1759) / skip 5924件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0853 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4280件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000407 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T18:36:16.165137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=85286.9
- Funnel: target 1076 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +111.41% | $4,748,072.68 |
| BTW/USDT:USDT | +4.14% | $24,445,722.87 |
| NEAR/USDT:USDT | +4.04% | $99,602,879.86 |
| VIRTUAL/USDT:USDT | +3.84% | $7,377,268.76 |
| PHA/USDT:USDT | +3.78% | $2,185,601.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.75% | +1.74% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.50% | +1.49% |
| FET/USDT:USDT | below_1h_threshold | +1.39% | +1.38% |
| VVV/USDT:USDT | below_1h_threshold | +1.19% | +1.18% |
| CRV/USDT:USDT | below_1h_threshold | +1.12% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
