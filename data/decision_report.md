# Decision Report

- generated_at: 2026-06-27T14:12:53.034670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7695, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +5.45% | **+0.82%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.53% | **+0.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.05% | **+0.32%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.13% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.15% | **+0.97%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.93%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.90% | **+0.78%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.52** / 初期 $100.00 (+132.52%)
- 確定: 2216件 (Win 662 / Loss 739 / Flat 815) / skip 2040件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $232.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.02** / 初期 $100.00 (+7.02%)
- 確定: 426件 (Win 115 / Loss 109 / Flat 202) / skip 680件
- 成長率目線: 平均log +0.000159 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score +0.0254 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.02

## 5. Latest Market Context

- 更新: 2026-06-27T14:12:47.459981+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=60556.3
- Funnel: target 806 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +116.76% | $153,174,293.43 |
| SYRUP/USDT:USDT | +29.51% | $3,050,683.72 |
| MYX/USDT:USDT | +26.12% | $17,014,884.57 |
| SLX/USDT:USDT | +21.94% | $9,038,174.36 |
| PUNDIX/USDT:USDT | +17.19% | $6,523,835.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +1.73% | +1.73% |
| WIF/USDT:USDT | below_1h_threshold | +1.52% | +1.52% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.17% | +1.16% |
| RE/USDT:USDT | below_1h_threshold | +0.54% | +0.54% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.53% | +0.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
