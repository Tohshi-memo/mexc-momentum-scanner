# Decision Report

- generated_at: 2026-06-17T23:09:57.858314+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6975**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=6975, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.07% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.48** / 初期 $100.00 (+1.48%)
- 確定トレード: 12件 (TP 5 / SL 7 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.48
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$199.69** / 初期 $100.00 (+99.69%)
- 確定: 1822件 (Win 497 / Loss 574 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $199.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定: 248件 (Win 65 / Loss 63 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.011% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0673 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.88

## 5. Latest Market Context

- 更新: 2026-06-17T23:09:52.771271+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64275.0
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +83.69% | $1,416,040.41 |
| ESPORTS/USDT:USDT | +43.31% | $18,510,172.02 |
| SYN/USDT:USDT | +43.17% | $4,089,358.46 |
| MITO/USDT:USDT | +14.54% | $1,633,136.68 |
| RE/USDT:USDT | +13.80% | $1,818,964.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +1.34% | +1.32% |
| STG/USDT:USDT | below_1h_threshold | +0.97% | +0.95% |
| MITO/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |
| APE/USDT:USDT | below_1h_threshold | +0.91% | +0.89% |
| SYN/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
