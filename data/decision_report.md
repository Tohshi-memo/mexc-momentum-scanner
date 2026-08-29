# Decision Report

- generated_at: 2026-08-29T07:26:17.544416+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12910**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.89% / filled 20/20。**
- 全期間 MARKET基準: n=12910, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.89% | **+2.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.89% | **+2.89%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.84% | **+2.42%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.16% | **+1.19%** |
| LIMIT_BB3S | 3/15 | 20.0% | +3.87% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.82% | **-0.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.71% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.83** / 初期 $100.00 (+608.83%)
- 確定: 4681件 (Win 1415 / Loss 1536 / Flat 1730) / skip 4790件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4318件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.53** / 初期 $100.00 (+16.53%)
- 確定: 2006件 (Win 589 / Loss 771 / Flat 646) / pending 2件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.53

## 6. Latest Market Context

- 更新: 2026-08-29T07:26:06.725904+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77496.7
- Funnel: target 1023 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +67.96% | $1,279,788.99 |
| HNT/USDT:USDT | +30.78% | $1,544,690.07 |
| BEAT/USDT:USDT | +23.86% | $14,350,857.71 |
| SKR/USDT:USDT | +16.70% | $1,585,897.85 |
| AKE/USDT:USDT | +13.53% | $20,281,184.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.53% | +3.45% |
| NIL/USDT:USDT | below_1h_threshold | +2.66% | +2.59% |
| COTI/USDT:USDT | below_1h_threshold | +1.54% | +1.47% |
| BTR/USDT:USDT | below_1h_threshold | +1.41% | +1.34% |
| TURBO/USDT:USDT | below_1h_threshold | +1.38% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
