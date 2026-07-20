# Decision Report

- generated_at: 2026-07-20T02:36:14.088301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9075**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=9075, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/18 | 11.1% | +5.43% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.52% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.12%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.30% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.27** / 初期 $100.00 (+298.27%)
- 確定: 3137件 (Win 984 / Loss 1001 / Flat 1152) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $398.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.74** / 初期 $100.00 (+25.74%)
- 確定: 1036件 (Win 266 / Loss 218 / Flat 552) / skip 1450件
- 成長率目線: 平均log +0.000221 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0914 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $125.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.90** / 初期 $100.00 (+0.90%)
- 確定: 274件 (Win 94 / Loss 131 / Flat 49) / pending 3件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.90

## 6. Latest Market Context

- 更新: 2026-07-20T02:36:07.572740+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=64750.1
- Funnel: target 885 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +45.36% | $87,265,865.07 |
| ACE/USDT:USDT | +44.75% | $3,110,215.99 |
| PUMPFUN/USDT:USDT | +20.94% | $17,044,037.65 |
| PROM/USDT:USDT | +18.80% | $2,100,515.13 |
| ANSEM/USDT:USDT | +14.02% | $1,890,075.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.94% | +3.70% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.38% | +3.14% |
| HOME/USDT:USDT | below_1h_threshold | +2.96% | +2.72% |
| B/USDT:USDT | below_1h_threshold | +2.92% | +2.68% |
| US/USDT:USDT | below_1h_threshold | +2.63% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
