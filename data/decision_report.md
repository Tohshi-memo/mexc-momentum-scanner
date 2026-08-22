# Decision Report

- generated_at: 2026-08-22T06:11:20.240614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12346**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.79% / filled 20/20。**
- 全期間 MARKET基準: n=12346, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+4.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.79% | **+4.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.79% | **+4.79%** |
| LIMIT_1PCT | 17/20 | 85.0% | +4.43% | **+3.77%** |
| LIMIT_ATR | 13/20 | 65.0% | +4.75% | **+3.08%** |
| LIMIT_2PCT | 11/20 | 55.0% | +3.06% | **+1.68%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_10PCT_LONG | 10/20 | 50.0% | +0.07% | **+0.03%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 15/20 | 75.0% | -0.49% | **-0.37%** |
| LIMIT_FIB1272_LONG | 17/20 | 85.0% | -0.85% | **-0.72%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.07** / 初期 $100.00 (+616.07%)
- 確定: 4447件 (Win 1364 / Loss 1453 / Flat 1630) / skip 4460件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3823件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.04** / 初期 $100.00 (+17.04%)
- 確定: 1862件 (Win 549 / Loss 705 / Flat 608) / pending 0件 / skip 1956件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.04

## 6. Latest Market Context

- 更新: 2026-08-22T06:11:09.996353+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77285.3
- Funnel: target 1018 → liquid 250 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +235.05% | $5,091,750.48 |
| TRUMPOFFICIAL/USDT:USDT | +53.55% | $97,208,934.92 |
| CATE/USDT:USDT | +40.88% | $11,525,808.50 |
| AGI/USDT:USDT | +35.02% | $1,915,405.47 |
| MELANIA/USDT:USDT | +32.03% | $1,431,921.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.74% | +1.86% |
| PROM/USDT:USDT | below_1h_threshold | +1.56% | +1.67% |
| CVX/USDT:USDT | below_1h_threshold | +1.22% | +1.33% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.86% | +0.98% |
| ZEN/USDT:USDT | below_1h_threshold | +0.75% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
