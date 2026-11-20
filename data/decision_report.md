# Decision Report

- generated_at: 2026-11-20T19:16:30.092347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19261**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=19261, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.02% | **-0.01%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.09% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,675.56** / 初期 $100.00 (+1575.56%)
- 確定: 7408件 (Win 2130 / Loss 2390 / Flat 2888) / skip 8414件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CBRSSTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,675.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.88** / 初期 $100.00 (+340.88%)
- 確定: 5081件 (Win 1353 / Loss 1087 / Flat 2641) / skip 7591件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $440.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000105 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T19:16:13.918128+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=58094.2
- Funnel: target 1087 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +28.57% | $24,862,993.68 |
| SKDD/USDT:USDT | +6.98% | $1,009,701.91 |
| PIEVERSE/USDT:USDT | +6.95% | $4,001,906.22 |
| OPENAI/USDT:USDT | +6.17% | $2,912,129.97 |
| SOXS/USDT:USDT | +5.98% | $86,357,068.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.60% | +3.09% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.73% | +2.22% |
| NGAS/USDT:USDT | below_1h_threshold | +1.70% | +2.18% |
| OPENAI/USDT:USDT | below_1h_threshold | +1.30% | +1.79% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
