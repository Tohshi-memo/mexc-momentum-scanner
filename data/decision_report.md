# Decision Report

- generated_at: 2026-09-22T18:41:29.554180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15352**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15352, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.45% | **+0.18%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.15% | **+0.11%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.01% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.41%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +2.01% | **+0.40%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.69% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.58** / 初期 $100.00 (+1067.58%)
- 確定: 5836件 (Win 1727 / Loss 1875 / Flat 2234) / skip 6077件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,167.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5410件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.80** / 初期 $100.00 (+22.80%)
- 確定: 3108件 (Win 913 / Loss 1217 / Flat 978) / pending 6件 / skip 3719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $122.80

## 6. Latest Market Context

- 更新: 2026-09-22T18:41:18.587545+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=86378.7
- Funnel: target 1058 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUBARAK/USDT:USDT | +19.02% | $13,368,387.93 |
| 4/USDT:USDT | +18.77% | $1,580,741.80 |
| MUSEBOOK/USDT:USDT | +18.31% | $1,078,115.61 |
| CHR/USDT:USDT | +18.09% | $3,714,060.13 |
| BR/USDT:USDT | +11.79% | $6,232,534.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.77% | +4.94% |
| AIN/USDT:USDT | below_1h_threshold | +4.19% | +4.36% |
| PENGU/USDT:USDT | below_1h_threshold | +2.49% | +2.66% |
| BEAT/USDT:USDT | below_1h_threshold | +1.92% | +2.09% |
| OP/USDT:USDT | below_1h_threshold | +1.87% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
