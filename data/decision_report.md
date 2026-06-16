# Decision Report

- generated_at: 2026-06-16T02:44:33.719605+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6832**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6832, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.27% | **-2.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.15% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.53% | **+0.27%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| ASK_LONG | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.12%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +3.18% | **+1.11%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.61% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.71** / 初期 $100.00 (+84.71%)
- 確定: 1705件 (Win 446 / Loss 531 / Flat 728) / skip 1688件
- 成長率目線: 平均log +0.000360 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account -0.01% 残高後 $184.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 88件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0671 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T02:44:29.378784+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.71% price=65841.8
- Funnel: target 772 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +40.04% | $7,349,115.90 |
| ROAM/USDT:USDT | +32.99% | $2,749,365.16 |
| PUFFER/USDT:USDT | +22.25% | $1,384,123.79 |
| SPCXSTOCK/USDT:USDT | +21.60% | $419,372,685.38 |
| VELVET/USDT:USDT | +15.61% | $12,140,787.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.62% | +5.33% |
| RIF/USDT:USDT | below_1h_threshold | +4.01% | +4.71% |
| BEAT/USDT:USDT | below_1h_threshold | +3.54% | +4.25% |
| ROAM/USDT:USDT | below_1h_threshold | +2.64% | +3.35% |
| ALLO/USDT:USDT | below_1h_threshold | +1.16% | +1.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
