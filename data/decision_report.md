# Decision Report

- generated_at: 2026-09-22T11:46:41.910239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15322**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15322, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 12/16 | 75.0% | +2.86% | **+2.15%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.35% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.06** / 初期 $100.00 (+1075.06%)
- 確定: 5813件 (Win 1725 / Loss 1870 / Flat 2218) / skip 6070件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,175.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.38** / 初期 $100.00 (+150.38%)
- 確定: 3352件 (Win 926 / Loss 780 / Flat 1646) / skip 5381件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $250.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.58** / 初期 $100.00 (+22.58%)
- 確定: 3093件 (Win 908 / Loss 1210 / Flat 975) / pending 4件 / skip 3697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000068 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.58

## 6. Latest Market Context

- 更新: 2026-09-22T11:46:32.296658+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=86076.6
- Funnel: target 1058 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +63.59% | $3,374,198.93 |
| MUBARAK/USDT:USDT | +41.98% | $4,517,951.62 |
| AGT/USDT:USDT | +38.11% | $1,774,381.44 |
| KERNEL/USDT:USDT | +33.75% | $4,540,973.73 |
| MARSCOIN/USDT:USDT | +24.81% | $1,955,920.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +3.26% | +3.01% |
| STX/USDT:USDT | below_1h_threshold | +2.50% | +2.25% |
| LAB/USDT:USDT | below_1h_threshold | +2.03% | +1.78% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.92% | +1.67% |
| TAO/USDT:USDT | below_1h_threshold | +1.74% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
