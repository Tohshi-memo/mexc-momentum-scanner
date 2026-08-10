# Decision Report

- generated_at: 2026-08-10T19:06:17.020868+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11191**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11191, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.30% | **+0.29%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.70% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.10% | **+0.88%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$619.87** / 初期 $100.00 (+519.87%)
- 確定: 3935件 (Win 1230 / Loss 1284 / Flat 1421) / skip 3817件
- 成長率目線: 平均log +0.000464 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $619.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3089件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1303件 (Win 404 / Loss 506 / Flat 393) / pending 0件 / skip 1361件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `MARKET` EXPIRED account +0.22% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T19:06:10.636672+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63875.8
- Funnel: target 962 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +58.08% | $3,856,617.62 |
| BTW/USDT:USDT | +9.12% | $7,744,273.92 |
| TST/USDT:USDT | +8.13% | $5,449,620.54 |
| CRV/USDT:USDT | +7.58% | $5,702,792.31 |
| UB/USDT:USDT | +7.53% | $1,437,647.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +1.73% | +1.72% |
| BANK/USDT:USDT | below_1h_threshold | +1.26% | +1.24% |
| ACT/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.13% | +1.12% |
| TUT/USDT:USDT | below_1h_threshold | +1.08% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
