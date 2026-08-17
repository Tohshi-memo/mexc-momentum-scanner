# Decision Report

- generated_at: 2026-08-17T04:16:41.198865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11795**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11795, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.27% | **+0.23%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.24% | **+0.23%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.41% | **+2.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.64% | **+0.41%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4184件 (Win 1292 / Loss 1363 / Flat 1529) / skip 4172件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.55** / 初期 $100.00 (+54.55%)
- 確定: 1802件 (Win 500 / Loss 422 / Flat 880) / skip 3404件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.06% 残高後 $154.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1599件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T04:16:31.983055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63467.4
- Funnel: target 986 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +40.29% | $15,889,245.02 |
| GPS/USDT:USDT | +31.81% | $2,610,164.00 |
| ACE/USDT:USDT | +24.76% | $15,909,871.47 |
| TUT/USDT:USDT | +23.45% | $4,916,947.73 |
| US/USDT:USDT | +15.81% | $1,577,570.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +3.90% | +3.81% |
| AIO/USDT:USDT | below_1h_threshold | +2.43% | +2.34% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.37% | +2.28% |
| HFT/USDT:USDT | below_1h_threshold | +2.32% | +2.22% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +2.22% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
