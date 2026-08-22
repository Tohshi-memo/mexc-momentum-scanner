# Decision Report

- generated_at: 2026-08-22T19:36:32.678431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12401**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=12401, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 7/18 | 38.9% | -0.30% | **-0.12%** |
| LIMIT_ATR | 11/20 | 55.0% | -0.22% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.80% | **+0.57%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.07** / 初期 $100.00 (+616.07%)
- 確定: 4447件 (Win 1364 / Loss 1453 / Flat 1630) / skip 4515件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3878件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000436 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-22T19:36:22.399532+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77345.9
- Funnel: target 1018 → liquid 210 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +20.86% | $15,708,566.98 |
| CATE/USDT:USDT | +19.32% | $10,511,409.46 |
| UAI/USDT:USDT | +12.73% | $2,714,881.73 |
| STX/USDT:USDT | +11.37% | $7,357,819.08 |
| DASH/USDT:USDT | +11.20% | $25,684,629.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +2.32% | +2.23% |
| CATE/USDT:USDT | below_1h_threshold | +1.95% | +1.86% |
| NEIROCTO/USDT:USDT | below_1h_threshold | +1.73% | +1.64% |
| FORM/USDT:USDT | below_1h_threshold | +1.69% | +1.60% |
| BICO/USDT:USDT | below_1h_threshold | +1.56% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
