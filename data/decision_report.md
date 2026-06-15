# Decision Report

- generated_at: 2026-06-15T06:03:29.755538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6751**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6751, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.70% | **+2.16%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.11% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.50** / 初期 $100.00 (+74.50%)
- 確定: 1624件 (Win 425 / Loss 503 / Flat 696) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BP/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $174.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.58** / 初期 $100.00 (-0.42%)
- 確定: 118件 (Win 25 / Loss 19 / Flat 74) / skip 44件
- 成長率目線: 平均log -0.000036 / 幾何平均 -0.004% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0441 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BP/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.58

## 5. Latest Market Context

- 更新: 2026-06-15T06:03:24.654398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=65830.0
- Funnel: target 770 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +101.57% | $3,213,145.59 |
| EVAA/USDT:USDT | +61.34% | $20,800,148.10 |
| CLO/USDT:USDT | +39.08% | $2,071,374.63 |
| GRASS/USDT:USDT | +21.02% | $1,467,627.73 |
| WLD/USDT:USDT | +18.12% | $108,787,138.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +1.31% | +1.31% |
| BP/USDT:USDT | below_1h_threshold | +0.83% | +0.82% |
| DASH/USDT:USDT | below_1h_threshold | +0.76% | +0.76% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| ORDI/USDT:USDT | below_1h_threshold | +0.46% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
