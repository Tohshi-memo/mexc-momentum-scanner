# Decision Report

- generated_at: 2026-11-17T03:51:19.633636+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19051**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.01% / filled 20/20。**
- 全期間 MARKET基準: n=19051, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.38% | **+1.17%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.72% | **+0.54%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7349件 (Win 2109 / Loss 2358 / Flat 2882) / skip 8263件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4990件 (Win 1332 / Loss 1081 / Flat 2577) / skip 7472件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7210件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000105 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-17T03:51:07.053390+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.76% price=64965.2
- Funnel: target 1069 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HUMA/USDT:USDT | +15.49% | $2,878,983.10 |
| LIT/USDT:USDT | +14.19% | $18,840,206.74 |
| BULLA/USDT:USDT | +12.25% | $1,754,691.47 |
| EVAA/USDT:USDT | +11.62% | $33,133,925.92 |
| NIGHT/USDT:USDT | +9.99% | $1,975,177.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.91% | +3.16% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.45% | +2.69% |
| SOPH/USDT:USDT | below_1h_threshold | +3.24% | +2.48% |
| BULLA/USDT:USDT | below_1h_threshold | +2.83% | +2.08% |
| LIT/USDT:USDT | below_1h_threshold | +2.65% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
