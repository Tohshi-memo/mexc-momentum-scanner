# Decision Report

- generated_at: 2026-08-29T08:11:19.834043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12912**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=12912, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.26% | **+1.92%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.99% | **+1.19%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.40% | **+0.91%** |
| LIMIT_BB3S | 4/15 | 26.7% | +2.46% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.36% | **-0.05%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.12% | **-0.06%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.07% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$713.31** / 初期 $100.00 (+613.31%)
- 確定: 4682件 (Win 1416 / Loss 1536 / Flat 1730) / skip 4791件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $713.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.18** / 初期 $100.00 (+57.18%)
- 確定: 2004件 (Win 545 / Loss 483 / Flat 976) / skip 4319件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $157.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.13** / 初期 $100.00 (+16.13%)
- 確定: 2008件 (Win 589 / Loss 773 / Flat 646) / pending 2件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.13

## 6. Latest Market Context

- 更新: 2026-08-29T08:11:08.806957+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=77474.3
- Funnel: target 1023 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +101.40% | $1,395,040.31 |
| HNT/USDT:USDT | +36.62% | $1,750,734.87 |
| BEAT/USDT:USDT | +24.42% | $15,838,167.56 |
| ONG/USDT:USDT | +19.24% | $3,227,106.04 |
| O/USDT:USDT | +15.54% | $1,008,173.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +3.07% | +3.22% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.20% | +2.34% |
| AKE/USDT:USDT | below_1h_threshold | +1.43% | +1.57% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.83% | +0.98% |
| MONAD/USDT:USDT | below_1h_threshold | +0.66% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
