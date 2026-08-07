# Decision Report

- generated_at: 2026-08-07T14:31:36.383044+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10720**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.13% / filled 20/20。**
- 全期間 MARKET基準: n=10720, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.14% | **+0.91%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.31% | **+0.14%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.20% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.66% | **-0.10%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.30% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3483件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2675件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.47** / 初期 $100.00 (+18.47%)
- 確定: 1168件 (Win 377 / Loss 458 / Flat 333) / pending 6件 / skip 1026件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000473 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DKNGSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.47

## 6. Latest Market Context

- 更新: 2026-08-07T14:31:27.515468+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=65090.3
- Funnel: target 961 → liquid 193 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 82.0 >= 65=1, 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +38.14% | $80,617,117.69 |
| CATE/USDT:USDT | +37.80% | $4,291,659.88 |
| BICO/USDT:USDT | +35.39% | $32,375,515.04 |
| TUT/USDT:USDT | +33.18% | $1,242,977.56 |
| C98/USDT:USDT | +30.71% | $1,774,903.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.52% | +4.35% |
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.38% | +4.22% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.03% | +2.87% |
| ALLO/USDT:USDT | below_1h_threshold | +2.13% | +1.96% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.06% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
