# Decision Report

- generated_at: 2026-06-15T01:09:20.662870+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6718**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=6718, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.96% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +6.51% | **+1.30%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| ASK_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.59** / 初期 $100.00 (+73.59%)
- 確定: 1591件 (Win 422 / Loss 498 / Flat 671) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $173.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 88件 (Win 21 / Loss 15 / Flat 52) / skip 41件
- 成長率目線: 平均log -0.000132 / 幾何平均 -0.013% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0511 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-15T01:09:15.756827+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=65453.0
- Funnel: target 770 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +44.47% | $6,558,368.84 |
| EVAA/USDT:USDT | +25.58% | $16,403,658.01 |
| RIF/USDT:USDT | +19.63% | $5,058,017.79 |
| LAB/USDT:USDT | +16.91% | $11,686,822.76 |
| EDEN/USDT:USDT | +14.93% | $1,424,515.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +2.60% | +2.81% |
| LAB/USDT:USDT | below_1h_threshold | +1.48% | +1.69% |
| EVAA/USDT:USDT | below_1h_threshold | +1.39% | +1.60% |
| AKT/USDT:USDT | below_1h_threshold | +1.33% | +1.54% |
| USELESS/USDT:USDT | below_1h_threshold | +1.32% | +1.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
