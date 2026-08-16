# Decision Report

- generated_at: 2026-08-16T00:56:21.001669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11705**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11705, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +2.78% | **+1.95%** |
| LIMIT_3PCT | 15/20 | 75.0% | +2.50% | **+1.88%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.10% | **+1.78%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.62% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.59%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$639.93** / 初期 $100.00 (+539.93%)
- 確定: 4173件 (Win 1291 / Loss 1356 / Flat 1526) / skip 4093件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $639.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1762件 (Win 493 / Loss 413 / Flat 856) / skip 3354件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1551件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000076 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T00:56:12.584515+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63039.8
- Funnel: target 985 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +20.38% | $3,965,169.16 |
| BULLA/USDT:USDT | +11.48% | $2,609,601.55 |
| CHIP/USDT:USDT | +10.30% | $1,391,406.39 |
| H/USDT:USDT | +9.37% | $5,869,614.76 |
| BTW/USDT:USDT | +7.44% | $11,185,386.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.56% | +4.58% |
| CROSS/USDT:USDT | below_1h_threshold | +3.47% | +3.49% |
| PRL/USDT:USDT | below_1h_threshold | +2.98% | +3.01% |
| CHIP/USDT:USDT | below_1h_threshold | +2.18% | +2.20% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.82% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
