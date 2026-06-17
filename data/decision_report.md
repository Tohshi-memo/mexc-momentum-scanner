# Decision Report

- generated_at: 2026-06-17T22:56:42.184699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6973**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=6973, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.48% | **+0.39%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.48** / 初期 $100.00 (+1.48%)
- 確定トレード: 12件 (TP 5 / SL 7 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.48
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1820件 (Win 496 / Loss 573 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.54** / 初期 $100.00 (+2.54%)
- 確定: 246件 (Win 64 / Loss 62 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000102 / 幾何平均 +0.010% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0601 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $102.54

## 5. Latest Market Context

- 更新: 2026-06-17T22:56:36.854802+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=64354.8
- Funnel: target 790 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +92.41% | $1,394,641.16 |
| ESPORTS/USDT:USDT | +66.21% | $17,472,137.49 |
| SYN/USDT:USDT | +41.53% | $4,045,393.29 |
| RE/USDT:USDT | +15.93% | $1,812,794.33 |
| MITO/USDT:USDT | +13.22% | $1,634,099.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +4.76% | +4.57% |
| TAC/USDT:USDT | below_1h_threshold | +4.17% | +3.98% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.51% | +2.31% |
| WLD/USDT:USDT | below_1h_threshold | +2.40% | +2.20% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.26% | +2.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
