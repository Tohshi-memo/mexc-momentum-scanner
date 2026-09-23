# Decision Report

- generated_at: 2026-09-23T00:01:26.979793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15374**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=15374, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.11% | **+1.79%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.09% | **+1.26%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_BB3S | 8/13 | 61.5% | +1.63% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.54% | **+1.42%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.55% | **+1.39%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.96% | **+0.98%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,161.60** / 初期 $100.00 (+1061.60%)
- 確定: 5852件 (Win 1730 / Loss 1880 / Flat 2242) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,161.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5432件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.36** / 初期 $100.00 (+22.36%)
- 確定: 3121件 (Win 918 / Loss 1224 / Flat 979) / pending 4件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000047 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FOLKS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.36

## 6. Latest Market Context

- 更新: 2026-09-23T00:01:15.392460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=86123.7
- Funnel: target 1058 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOLKS/USDT:USDT | +35.98% | $3,111,290.97 |
| DRIFT/USDT:USDT | +27.83% | $1,682,832.77 |
| 4/USDT:USDT | +21.52% | $2,425,491.80 |
| ALLO/USDT:USDT | +16.19% | $1,966,928.58 |
| MARSCOIN/USDT:USDT | +16.12% | $3,473,628.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +0.97% | +1.01% |
| KERNEL/USDT:USDT | below_1h_threshold | +0.57% | +0.61% |
| MYX/USDT:USDT | below_1h_threshold | +0.56% | +0.60% |
| MUU/USDT:USDT | below_1h_threshold | +0.49% | +0.53% |
| LAB/USDT:USDT | below_1h_threshold | +0.38% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
