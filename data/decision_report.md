# Decision Report

- generated_at: 2026-11-16T09:31:26.993558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=19005, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.03% | **+0.60%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.65% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.32% | **+0.25%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.36% | **+0.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,694.26** / 初期 $100.00 (+1594.26%)
- 確定: 7346件 (Win 2109 / Loss 2356 / Flat 2881) / skip 8220件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,694.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4984件 (Win 1332 / Loss 1081 / Flat 2571) / skip 7432件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHELL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7165件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T09:31:14.300430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64310.0
- Funnel: target 1066 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1, 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +83.33% | $10,359,786.32 |
| SKR/USDT:USDT | +27.05% | $4,107,531.58 |
| BLESS/USDT:USDT | +24.70% | $1,647,485.97 |
| EVAA/USDT:USDT | +22.58% | $20,620,977.47 |
| PIEVERSE/USDT:USDT | +7.28% | $1,751,388.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHELL/USDT:USDT | below_1h_threshold | +3.35% | +3.54% |
| EVAA/USDT:USDT | below_1h_threshold | +2.57% | +2.76% |
| BARD/USDT:USDT | below_1h_threshold | +1.00% | +1.19% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.75% | +0.93% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.38% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
