# Decision Report

- generated_at: 2026-09-21T07:46:32.003996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15238**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=15238, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.63% | **+1.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.22% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.81% | **+0.61%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.63% | **+0.74%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,170.76** / 初期 $100.00 (+1070.76%)
- 確定: 5729件 (Win 1707 / Loss 1846 / Flat 2176) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,170.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.99** / 初期 $100.00 (+146.99%)
- 確定: 3301件 (Win 912 / Loss 765 / Flat 1624) / skip 5348件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0128 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $246.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.23** / 初期 $100.00 (+22.23%)
- 確定: 3016件 (Win 890 / Loss 1186 / Flat 940) / pending 4件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.23

## 6. Latest Market Context

- 更新: 2026-09-21T07:46:20.923441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=81494.7
- Funnel: target 1050 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=2
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +66.33% | $3,829,582.13 |
| NIL/USDT:USDT | +32.22% | $7,007,498.01 |
| PTB/USDT:USDT | +24.69% | $1,062,867.33 |
| MINA/USDT:USDT | +22.93% | $1,086,646.81 |
| SEI/USDT:USDT | +18.64% | $18,329,278.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.07% | +3.21% |
| SAGA/USDT:USDT | below_1h_threshold | +2.71% | +2.85% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.46% | +2.60% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.07% | +2.21% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.03% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
