# Decision Report

- generated_at: 2026-08-15T03:26:24.650782+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11628**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=11628, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.31% | **+0.66%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.48%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$642.60** / 初期 $100.00 (+542.60%)
- 確定: 4096件 (Win 1284 / Loss 1349 / Flat 1463) / skip 4093件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $642.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.49** / 初期 $100.00 (+52.49%)
- 確定: 1691件 (Win 483 / Loss 409 / Flat 799) / skip 3348件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $152.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.31** / 初期 $100.00 (+17.31%)
- 確定: 1575件 (Win 479 / Loss 604 / Flat 492) / pending 4件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.31

## 6. Latest Market Context

- 更新: 2026-08-15T03:26:14.806161+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63072.1
- Funnel: target 985 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +25.85% | $2,526,575.76 |
| US/USDT:USDT | +17.22% | $6,788,115.95 |
| CAP/USDT:USDT | +16.19% | $22,342,217.53 |
| AIO/USDT:USDT | +14.71% | $1,356,141.92 |
| CYS/USDT:USDT | +14.15% | $15,927,449.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.55% | +3.62% |
| BR/USDT:USDT | below_1h_threshold | +2.26% | +2.33% |
| CAP/USDT:USDT | below_1h_threshold | +2.10% | +2.17% |
| AIO/USDT:USDT | below_1h_threshold | +1.63% | +1.70% |
| DOLO/USDT:USDT | below_1h_threshold | +1.57% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
