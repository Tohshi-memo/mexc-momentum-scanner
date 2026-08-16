# Decision Report

- generated_at: 2026-08-16T00:46:19.837673+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11704**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11704, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +2.53% | **+1.90%** |
| LIMIT_3PCT | 16/20 | 80.0% | +2.29% | **+1.83%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.87% | **+1.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.62% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.59%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.46%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.59% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$639.93** / 初期 $100.00 (+539.93%)
- 確定: 4172件 (Win 1291 / Loss 1356 / Flat 1525) / skip 4093件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $639.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1761件 (Win 493 / Loss 413 / Flat 855) / skip 3354件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1551件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000119 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T00:46:11.546454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63041.3
- Funnel: target 985 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +17.42% | $3,917,475.05 |
| CHIP/USDT:USDT | +12.57% | $1,353,614.31 |
| H/USDT:USDT | +9.88% | $5,804,897.52 |
| BULLA/USDT:USDT | +9.65% | $2,597,625.65 |
| BTW/USDT:USDT | +8.25% | $11,160,886.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +4.36% | +4.38% |
| CROSS/USDT:USDT | below_1h_threshold | +4.36% | +4.38% |
| AEON1/USDT:USDT | below_1h_threshold | +3.13% | +3.15% |
| PRL/USDT:USDT | below_1h_threshold | +2.96% | +2.98% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.23% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
