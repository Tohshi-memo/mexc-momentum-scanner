# Decision Report

- generated_at: 2026-09-22T05:01:23.816519+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15296**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=15296, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.25% | **+2.02%** |
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_BB3S | 7/18 | 38.9% | +3.00% | **+1.17%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.37% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.53% | **+0.24%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.23% | **+0.10%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -0.67% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.99** / 初期 $100.00 (+1074.99%)
- 確定: 5787件 (Win 1721 / Loss 1863 / Flat 2203) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WLD/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.21% 残高後 $1,174.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.31** / 初期 $100.00 (+148.31%)
- 確定: 3335件 (Win 921 / Loss 774 / Flat 1640) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: WLD/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.16% 残高後 $248.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.67** / 初期 $100.00 (+22.67%)
- 確定: 3068件 (Win 902 / Loss 1201 / Flat 965) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WLD/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.08% 残高後 $122.67

## 6. Latest Market Context

- 更新: 2026-09-22T05:01:13.434432+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=85400.1
- Funnel: target 1057 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +34.34% | $3,056,914.21 |
| MUBARAK/USDT:USDT | +20.74% | $1,791,757.51 |
| GRASS/USDT:USDT | +18.68% | $2,634,317.79 |
| ALCH/USDT:USDT | +18.62% | $2,495,239.71 |
| NIL/USDT:USDT | +10.94% | $3,925,568.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.12% | +2.14% |
| MUBARAK/USDT:USDT | below_1h_threshold | +0.88% | +0.91% |
| 4STOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.53% |
| USOIL/USDT:USDT | below_1h_threshold | +0.42% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
