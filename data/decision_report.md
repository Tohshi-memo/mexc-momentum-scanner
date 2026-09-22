# Decision Report

- generated_at: 2026-09-22T21:46:18.830508+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15363**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15363, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.66% | **+0.50%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.43% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_BB3S | 9/15 | 60.0% | +0.45% | **+0.27%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.65% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.60% | **+1.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +2.66% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.82** / 初期 $100.00 (+1055.82%)
- 確定: 5846件 (Win 1729 / Loss 1880 / Flat 2237) / skip 6078件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,155.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5421件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.15** / 初期 $100.00 (+22.15%)
- 確定: 3115件 (Win 914 / Loss 1222 / Flat 979) / pending 5件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.15

## 6. Latest Market Context

- 更新: 2026-09-22T21:46:09.640327+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=86165.2
- Funnel: target 1058 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +30.78% | $1,092,008.27 |
| FOLKS/USDT:USDT | +25.76% | $1,827,549.15 |
| DRIFT/USDT:USDT | +25.69% | $1,566,449.82 |
| 4/USDT:USDT | +20.32% | $2,131,572.93 |
| PONS/USDT:USDT | +15.95% | $4,928,169.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.58% | +4.66% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.73% | +2.81% |
| ALLO/USDT:USDT | below_1h_threshold | +2.31% | +2.38% |
| SAGA/USDT:USDT | below_1h_threshold | +2.21% | +2.29% |
| 4/USDT:USDT | below_1h_threshold | +2.10% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
