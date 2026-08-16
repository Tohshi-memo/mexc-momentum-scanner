# Decision Report

- generated_at: 2026-08-16T00:06:24.151942+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11702, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.78% | **+1.33%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.31% | **+1.11%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.70% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.10% | **+0.50%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +0.53% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.15** / 初期 $100.00 (+543.15%)
- 確定: 4170件 (Win 1291 / Loss 1355 / Flat 1524) / skip 4093件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $643.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1760件 (Win 493 / Loss 413 / Flat 854) / skip 3353件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 1625件 (Win 495 / Loss 617 / Flat 513) / pending 1件 / skip 1550件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000077 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-08-16T00:06:15.644988+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63044.7
- Funnel: target 985 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +32.96% | $3,337,240.86 |
| HEMI/USDT:USDT | +10.93% | $3,983,166.25 |
| BULLA/USDT:USDT | +10.28% | $2,526,217.60 |
| H/USDT:USDT | +9.26% | $5,632,842.48 |
| AIO/USDT:USDT | +7.98% | $2,720,842.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +4.07% | +4.08% |
| HEMI/USDT:USDT | below_1h_threshold | +3.53% | +3.54% |
| ROBO/USDT:USDT | below_1h_threshold | +1.85% | +1.86% |
| H/USDT:USDT | below_1h_threshold | +0.94% | +0.96% |
| ALLO/USDT:USDT | below_1h_threshold | +0.72% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
