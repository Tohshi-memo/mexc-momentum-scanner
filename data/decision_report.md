# Decision Report

- generated_at: 2026-06-15T22:15:01.389043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6816**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=6816, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +3.23% | **+1.61%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.88% | **+0.58%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.49% | **+1.12%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.97% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$103.53** / 初期 $100.00 (+3.53%)
- 確定トレード: 8件 (TP 5 / SL 3 / EXP 0)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.53
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$180.15** / 初期 $100.00 (+80.15%)
- 確定: 1689件 (Win 442 / Loss 528 / Flat 719) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $180.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 72件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T22:14:57.149698+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=66348.1
- Funnel: target 772 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +31.99% | $2,434,298.76 |
| EVAA/USDT:USDT | +19.45% | $41,801,884.98 |
| HOME/USDT:USDT | +13.41% | $1,091,863.97 |
| SPCXSTOCK/USDT:USDT | +11.65% | $258,555,126.68 |
| FOLKS/USDT:USDT | +9.79% | $2,286,266.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.99% | +3.97% |
| BTW/USDT:USDT | below_1h_threshold | +1.90% | +1.88% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.60% | +1.59% |
| BABY/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| SIREN/USDT:USDT | below_1h_threshold | +0.89% | +0.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
