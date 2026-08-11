# Decision Report

- generated_at: 2026-08-11T03:16:23.169125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11212**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.17% / filled 20/20。**
- 全期間 MARKET基準: n=11212, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.55% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.36% | **+0.23%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.12% | **+0.08%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.32% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3936件 (Win 1230 / Loss 1285 / Flat 1421) / skip 3837件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3109件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.08** / 初期 $100.00 (+17.08%)
- 確定: 1310件 (Win 406 / Loss 511 / Flat 393) / pending 3件 / skip 1370件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SQD/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.08

## 6. Latest Market Context

- 更新: 2026-08-11T03:16:13.355394+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64074.7
- Funnel: target 962 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +89.29% | $16,176,405.87 |
| TOAD/USDT:USDT | +53.08% | $1,172,899.83 |
| CYS/USDT:USDT | +14.56% | $23,804,496.60 |
| CRV/USDT:USDT | +12.45% | $9,026,564.75 |
| COOKIE/USDT:USDT | +11.55% | $1,397,479.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COOKIE/USDT:USDT | below_1h_threshold | +4.74% | +4.65% |
| HEI/USDT:USDT | below_1h_threshold | +4.66% | +4.56% |
| BLESS/USDT:USDT | below_1h_threshold | +4.30% | +4.20% |
| EPIC/USDT:USDT | below_1h_threshold | +1.92% | +1.82% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.48% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
