# Decision Report

- generated_at: 2026-06-16T02:04:45.138939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6828**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6828, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.91% | **-2.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 14/20 | 70.0% | +0.28% | **+0.20%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.01% | **+0.00%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.47% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| ASK_LONG | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.68% | **+1.87%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.27% | **+1.64%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.44% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$183.82** / 初期 $100.00 (+83.82%)
- 確定: 1701件 (Win 445 / Loss 529 / Flat 727) / skip 1688件
- 成長率目線: 平均log +0.000358 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $183.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 84件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0622 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T02:04:40.976747+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=66314.5
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +35.41% | $7,084,575.04 |
| ROAM/USDT:USDT | +30.89% | $2,709,069.84 |
| PUFFER/USDT:USDT | +23.36% | $1,321,827.94 |
| SPCXSTOCK/USDT:USDT | +22.61% | $396,015,839.79 |
| SPACE/USDT:USDT | +20.31% | $1,122,721.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +2.05% | +2.04% |
| SPACE/USDT:USDT | below_1h_threshold | +1.51% | +1.50% |
| EVAA/USDT:USDT | below_1h_threshold | +1.32% | +1.31% |
| ROAM/USDT:USDT | below_1h_threshold | +1.18% | +1.18% |
| AKT/USDT:USDT | below_1h_threshold | +1.01% | +1.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
