# Decision Report

- generated_at: 2026-07-30T16:06:31.854949+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9904**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9904, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.85% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.52% | **+2.52%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.96% | **+1.93%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.27% | **+1.64%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +1.37% | **+0.41%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2945件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2072件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.01** / 初期 $100.00 (+11.01%)
- 確定: 800件 (Win 261 / Loss 316 / Flat 223) / pending 5件 / skip 586件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000302 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.01

## 6. Latest Market Context

- 更新: 2026-07-30T16:06:23.416875+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=64831.2
- Funnel: target 920 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +2.98% | $2,055,968.99 |
| JIMOTHY/USDT:USDT | +2.61% | $2,228,038.14 |
| ZHIPUSTOCK/USDT:USDT | +2.53% | $3,921,037.07 |
| ARMSTOCK/USDT:USDT | +2.40% | $1,389,684.49 |
| COTI/USDT:USDT | +2.31% | $18,922,816.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.98% | +2.77% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.66% | +2.45% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.63% | +2.42% |
| MUU/USDT:USDT | below_1h_threshold | +2.43% | +2.21% |
| COTI/USDT:USDT | below_1h_threshold | +2.29% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
