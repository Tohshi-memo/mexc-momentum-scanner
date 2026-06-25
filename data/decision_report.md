# Decision Report

- generated_at: 2026-06-25T22:12:30.250194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7588**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7588, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |
| ASK | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.11% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.21% | **+1.09%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.59% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$103.17** / 初期 $100.00 (+3.17%)
- 確定トレード: 40件 (TP 15 / SL 24 / EXP 1)
- 最新: DRAM/USDT:USDT EXPIRED PnL +1.79% 残高後 $103.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2017件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 377件 (Win 103 / Loss 100 / Flat 174) / skip 622件
- 成長率目線: 平均log +0.000194 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-25T22:12:25.667631+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=59938.3
- Funnel: target 807 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOGO/USDT:USDT | +17.50% | $1,939,893.81 |
| IP/USDT:USDT | +15.38% | $2,475,265.12 |
| IDOL/USDT:USDT | +12.62% | $1,569,792.76 |
| AIN/USDT:USDT | +10.65% | $1,576,551.20 |
| HEI/USDT:USDT | +8.39% | $5,869,322.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.11% | +1.52% |
| BAS/USDT:USDT | below_1h_threshold | +0.56% | +0.96% |
| UB/USDT:USDT | below_1h_threshold | +0.43% | +0.84% |
| AIN/USDT:USDT | below_1h_threshold | +0.40% | +0.81% |
| IDOL/USDT:USDT | below_1h_threshold | +0.40% | +0.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
