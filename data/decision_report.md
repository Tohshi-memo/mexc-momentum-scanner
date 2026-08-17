# Decision Report

- generated_at: 2026-08-17T02:46:30.619066+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11788**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=11788, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.68% | **+1.09%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.03% | **+0.92%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.04% | **+0.83%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.91% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.12% | **-0.05%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.38% | **-0.38%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -1.10% | **-0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4184件 (Win 1292 / Loss 1363 / Flat 1529) / skip 4165件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.35** / 初期 $100.00 (+54.35%)
- 確定: 1795件 (Win 498 / Loss 420 / Flat 877) / skip 3404件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.06% 残高後 $154.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1588件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T02:46:17.828432+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=63229.0
- Funnel: target 986 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +35.88% | $15,255,130.38 |
| BTW/USDT:USDT | +17.25% | $34,233,449.63 |
| HFT/USDT:USDT | +16.91% | $2,642,699.99 |
| GPS/USDT:USDT | +16.55% | $2,031,694.35 |
| ONG/USDT:USDT | +14.38% | $1,365,938.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.00% | +3.77% |
| GPS/USDT:USDT | below_1h_threshold | +3.63% | +3.40% |
| HFT/USDT:USDT | below_1h_threshold | +3.45% | +3.22% |
| NIL/USDT:USDT | below_1h_threshold | +2.55% | +2.32% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.12% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
