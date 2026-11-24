# Decision Report

- generated_at: 2026-11-24T22:06:23.497573+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19581**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=19581, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.53% | **+1.45%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.55% | **+0.30%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.46% | **+0.26%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 287件 (TP 105 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,989.52** / 初期 $100.00 (+1889.52%)
- 確定: 7609件 (Win 2191 / Loss 2449 / Flat 2969) / skip 8533件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,989.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7772件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0021 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7743件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000057 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T22:06:10.786245+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=60013.6
- Funnel: target 1092 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +22.53% | $1,485,517.79 |
| BTW/USDT:USDT | +6.59% | $3,218,963.34 |
| SNXX/USDT:USDT | +6.53% | $41,001,066.04 |
| IRYS/USDT:USDT | +5.45% | $1,561,975.42 |
| SOXL/USDT:USDT | +5.33% | $1,564,230,822.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +1.96% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.59% | +1.35% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.06% | +0.82% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.45% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
