# Decision Report

- generated_at: 2026-06-16T01:11:09.218181+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6822**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6822, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.85% | **+0.26%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.51% | **+0.26%** |
| LIMIT_6PCT | 3/20 | 15.0% | +0.10% | **+0.02%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.34% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$182.91** / 初期 $100.00 (+82.91%)
- 確定: 1695件 (Win 444 / Loss 528 / Flat 723) / skip 1688件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $182.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 78件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T01:11:04.909534+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=66284.8
- Funnel: target 772 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +25.49% | $2,675,208.14 |
| ASTEROID/USDT:USDT | +23.74% | $6,770,335.12 |
| SPCXSTOCK/USDT:USDT | +22.57% | $357,091,676.54 |
| EVAA/USDT:USDT | +18.95% | $41,912,388.58 |
| FOLKS/USDT:USDT | +18.53% | $2,495,562.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.08% | +3.98% |
| BTW/USDT:USDT | below_1h_threshold | +3.20% | +3.10% |
| COAI/USDT:USDT | below_1h_threshold | +1.65% | +1.55% |
| SIREN/USDT:USDT | below_1h_threshold | +1.64% | +1.54% |
| CRV/USDT:USDT | below_1h_threshold | +1.35% | +1.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
