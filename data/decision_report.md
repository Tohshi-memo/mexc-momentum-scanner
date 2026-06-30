# Decision Report

- generated_at: 2026-06-30T02:00:48.070689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7846**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=7846, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.62% | **+0.49%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.64% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.38% | **+0.32%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.50% | **+0.15%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.10% | **+0.08%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.44** / 初期 $100.00 (+160.44%)
- 確定: 2350件 (Win 714 / Loss 784 / Flat 852) / skip 2057件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $260.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 800件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T02:00:43.244405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=59916.9
- Funnel: target 811 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +35.23% | $1,805,260.46 |
| AIGENSYN/USDT:USDT | +26.69% | $3,717,424.14 |
| ANSEM/USDT:USDT | +23.06% | $1,016,944.40 |
| SYN/USDT:USDT | +21.60% | $22,280,399.53 |
| H/USDT:USDT | +19.94% | $7,507,691.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +0.88% | +0.88% |
| SYN/USDT:USDT | below_1h_threshold | +0.83% | +0.83% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.82% | +0.82% |
| H/USDT:USDT | below_1h_threshold | +0.40% | +0.40% |
| UB/USDT:USDT | below_1h_threshold | +0.33% | +0.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
