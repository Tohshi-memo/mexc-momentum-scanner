# Decision Report

- generated_at: 2026-06-16T03:04:55.526838+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6834**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6834, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.66% | **-1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.87% | **+0.88%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.15% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| ASK_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.38% | **+1.18%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.20% | **+0.90%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.79% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$183.79** / 初期 $100.00 (+83.79%)
- 確定: 1707件 (Win 446 / Loss 532 / Flat 729) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $183.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 90件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0579 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T03:04:49.680076+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=65791.6
- Funnel: target 772 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +47.98% | $7,442,955.97 |
| ROAM/USDT:USDT | +34.05% | $2,759,728.50 |
| SPCXSTOCK/USDT:USDT | +20.88% | $429,276,194.02 |
| PUFFER/USDT:USDT | +18.30% | $1,401,285.97 |
| SPACE/USDT:USDT | +13.19% | $1,460,120.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.14% | +2.02% |
| EVAA/USDT:USDT | below_1h_threshold | +2.04% | +1.92% |
| BTW/USDT:USDT | below_1h_threshold | +1.27% | +1.15% |
| SPX/USDT:USDT | below_1h_threshold | +0.95% | +0.83% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.89% | +0.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
