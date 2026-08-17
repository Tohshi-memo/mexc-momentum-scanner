# Decision Report

- generated_at: 2026-08-17T01:06:18.044535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11781**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.12% / filled 20/20。**
- 全期間 MARKET基準: n=11781, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.86% | **+2.57%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.41% | **+0.92%** |
| LIMIT_BB3S | 3/16 | 18.8% | +4.55% | **+0.85%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.38% | **-0.21%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.78% | **-0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4159件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.30** / 初期 $100.00 (+54.30%)
- 確定: 1789件 (Win 496 / Loss 419 / Flat 874) / skip 3403件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0459 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.11% 残高後 $154.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1578件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000294 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T01:06:09.604130+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=63085.4
- Funnel: target 986 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +25.09% | $13,981,922.34 |
| HFT/USDT:USDT | +22.11% | $2,571,444.56 |
| BTW/USDT:USDT | +17.91% | $27,420,094.61 |
| US/USDT:USDT | +9.46% | $1,744,311.75 |
| ONG/USDT:USDT | +8.41% | $1,009,608.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +2.95% | +2.64% |
| HFT/USDT:USDT | below_1h_threshold | +2.46% | +2.14% |
| SNXX/USDT:USDT | below_1h_threshold | +2.24% | +1.93% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.14% | +1.83% |
| GPS/USDT:USDT | below_1h_threshold | +1.49% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
