# Decision Report

- generated_at: 2026-08-12T08:01:22.484076+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11342**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=11342, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.21% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +4.58% | **+2.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.28% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3963件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$146.16** / 初期 $100.00 (+46.16%)
- 確定: 1578件 (Win 441 / Loss 365 / Flat 772) / skip 3175件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0616 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $146.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.07** / 初期 $100.00 (+14.07%)
- 確定: 1357件 (Win 409 / Loss 530 / Flat 418) / pending 3件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $114.07

## 6. Latest Market Context

- 更新: 2026-08-12T08:01:13.002561+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63792.3
- Funnel: target 967 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +81.75% | $2,224,517.78 |
| APR/USDT:USDT | +64.74% | $1,418,536.88 |
| PROM/USDT:USDT | +31.44% | $6,940,349.80 |
| BEAT/USDT:USDT | +18.56% | $87,408,914.32 |
| CRWVSTOCK/USDT:USDT | +17.72% | $4,413,230.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.68% | +3.70% |
| SNXX/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.78% | +0.80% |
| KORU/USDT:USDT | below_1h_threshold | +0.75% | +0.77% |
| BEAT/USDT:USDT | below_1h_threshold | +0.61% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
