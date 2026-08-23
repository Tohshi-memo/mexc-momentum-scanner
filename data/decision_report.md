# Decision Report

- generated_at: 2026-08-23T01:16:23.582263+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12430**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=12430, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.08% | **+0.63%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.56% | **+0.54%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.53% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +8.00% | **+5.33%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.81% | **+1.27%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.58% | **+1.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$699.18** / 初期 $100.00 (+599.18%)
- 確定: 4459件 (Win 1365 / Loss 1458 / Flat 1636) / skip 4532件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $699.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3906件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2040件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000110 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T01:16:12.717277+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77399.9
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +50.05% | $12,961,076.37 |
| TUT/USDT:USDT | +38.81% | $42,850,063.16 |
| ZRO/USDT:USDT | +15.47% | $9,198,237.27 |
| STX/USDT:USDT | +14.28% | $10,003,802.37 |
| UAI/USDT:USDT | +11.78% | $3,093,820.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +3.19% | +3.07% |
| TUT/USDT:USDT | below_1h_threshold | +2.04% | +1.92% |
| DASH/USDT:USDT | below_1h_threshold | +1.96% | +1.84% |
| ONG/USDT:USDT | below_1h_threshold | +1.73% | +1.61% |
| ARX/USDT:USDT | below_1h_threshold | +1.66% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
