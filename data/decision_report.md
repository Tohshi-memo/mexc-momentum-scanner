# Decision Report

- generated_at: 2026-11-06T01:21:26.919110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18219**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=18219, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.67% | **+1.50%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.84% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.60% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.21% | **+1.10%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.40% | **+0.63%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,507.12** / 初期 $100.00 (+1407.12%)
- 確定: 7022件 (Win 2022 / Loss 2243 / Flat 2757) / skip 7758件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,507.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$375.26** / 初期 $100.00 (+275.26%)
- 確定: 4611件 (Win 1235 / Loss 1030 / Flat 2346) / skip 7019件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $375.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6378件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T01:21:11.545905+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=76197.1
- Funnel: target 1084 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYBER/USDT:USDT | +37.45% | $1,503,702.49 |
| IRENSTOCK/USDT:USDT | +16.13% | $3,099,675.54 |
| BLESS/USDT:USDT | +13.66% | $5,375,822.42 |
| UVXY/USDT:USDT | +11.87% | $3,073,866.54 |
| BTW/USDT:USDT | +11.76% | $6,287,486.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.40% | +4.53% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +3.89% | +4.03% |
| JCT/USDT:USDT | below_1h_threshold | +3.66% | +3.80% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.64% | +3.78% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.60% | +3.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
