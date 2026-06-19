# Decision Report

- generated_at: 2026-06-19T01:35:47.568837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7091**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7091, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.33% | **+0.43%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.82% | **-0.29%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.90% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.16% | **+1.62%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.50% | **+1.42%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.26% | **+0.75%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.29** / 初期 $100.00 (+123.29%)
- 確定: 1911件 (Win 545 / Loss 613 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $223.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 194件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T01:35:43.097047+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=62830.0
- Funnel: target 795 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +95.33% | $5,695,447.16 |
| BASED/USDT:USDT | +28.42% | $3,508,672.01 |
| ZEREBRO/USDT:USDT | +25.54% | $3,241,277.16 |
| EDEN/USDT:USDT | +16.68% | $2,117,849.96 |
| EIGEN/USDT:USDT | +13.02% | $3,372,007.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.21% | +3.46% |
| BASED/USDT:USDT | below_1h_threshold | +2.66% | +2.91% |
| TAC/USDT:USDT | below_1h_threshold | +2.29% | +2.54% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.56% |
| CHIP/USDT:USDT | below_1h_threshold | +0.97% | +1.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
