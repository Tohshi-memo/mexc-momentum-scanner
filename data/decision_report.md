# Decision Report

- generated_at: 2026-08-12T06:56:24.107473+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11336**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=11336, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.59% | **+1.28%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.68% | **+0.58%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.96% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +5.72% | **+2.86%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.53% | **+0.35%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.64% | **+0.26%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.10% | **+0.05%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3957件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.06** / 初期 $100.00 (+44.06%)
- 確定: 1573件 (Win 438 / Loss 364 / Flat 771) / skip 3174件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $144.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.27** / 初期 $100.00 (+14.27%)
- 確定: 1351件 (Win 409 / Loss 529 / Flat 413) / pending 3件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000077 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FHE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.27

## 6. Latest Market Context

- 更新: 2026-08-12T06:56:14.440991+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=63609.4
- Funnel: target 968 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +27.38% | $92,429,270.89 |
| PROM/USDT:USDT | +27.26% | $6,909,501.36 |
| JIMOTHY/USDT:USDT | +21.45% | $2,021,827.68 |
| CRWVSTOCK/USDT:USDT | +17.41% | $4,306,686.83 |
| BTW/USDT:USDT | +11.14% | $4,867,878.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +3.34% | +3.67% |
| FHE/USDT:USDT | below_1h_threshold | +3.07% | +3.39% |
| BEAT/USDT:USDT | below_1h_threshold | +2.81% | +3.13% |
| GRVT/USDT:USDT | below_1h_threshold | +2.13% | +2.45% |
| XMR/USDT:USDT | below_1h_threshold | +1.42% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
