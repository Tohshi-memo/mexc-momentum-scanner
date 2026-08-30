# Decision Report

- generated_at: 2026-08-30T12:26:22.378375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13057**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13057, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.64% | **+0.55%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.18% | **+2.18%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.21% | **+0.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$774.74** / 初期 $100.00 (+674.74%)
- 確定: 4807件 (Win 1463 / Loss 1584 / Flat 1760) / skip 4811件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $774.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.79** / 初期 $100.00 (+71.79%)
- 確定: 2141件 (Win 593 / Loss 519 / Flat 1029) / skip 4327件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $171.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 2080件 (Win 610 / Loss 809 / Flat 661) / pending 3件 / skip 2446件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-30T12:26:12.911772+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=78479.6
- Funnel: target 1026 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +108.54% | $7,319,810.46 |
| HNT/USDT:USDT | +96.98% | $44,198,585.76 |
| ZKC/USDT:USDT | +55.36% | $4,716,097.16 |
| PONS/USDT:USDT | +54.62% | $1,794,350.63 |
| SKR/USDT:USDT | +48.71% | $3,758,114.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_relative_strength | +5.26% | +4.83% |
| HNT/USDT:USDT | below_1h_threshold | +3.53% | +3.10% |
| LAB/USDT:USDT | below_1h_threshold | +2.65% | +2.22% |
| DEXE/USDT:USDT | below_1h_threshold | +2.47% | +2.04% |
| SPX/USDT:USDT | below_1h_threshold | +1.99% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
