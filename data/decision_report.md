# Decision Report

- generated_at: 2026-09-23T02:21:20.642867+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15382**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.74% / filled 20/20。**
- 全期間 MARKET基準: n=15382, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.61% | **+0.81%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.91% | **+0.54%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.03% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.46% | **+0.51%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.16% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.35** / 初期 $100.00 (+1067.35%)
- 確定: 5860件 (Win 1731 / Loss 1881 / Flat 2248) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $1,167.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5440件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.56** / 初期 $100.00 (+22.56%)
- 確定: 3123件 (Win 919 / Loss 1225 / Flat 979) / pending 6件 / skip 3727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.56

## 6. Latest Market Context

- 更新: 2026-09-23T02:21:09.452695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=86477.3
- Funnel: target 1058 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +70.63% | $1,082,529.41 |
| ALLO/USDT:USDT | +17.79% | $2,423,131.19 |
| FOLKS/USDT:USDT | +17.67% | $6,093,487.72 |
| DRIFT/USDT:USDT | +15.01% | $1,772,167.56 |
| UNI/USDT:USDT | +14.98% | $53,704,335.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.62% | +4.44% |
| 4STOCK/USDT:USDT | below_1h_threshold | +4.61% | +4.43% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.26% | +3.08% |
| MUBARAK/USDT:USDT | below_1h_threshold | +3.05% | +2.87% |
| BTW/USDT:USDT | below_1h_threshold | +1.73% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
