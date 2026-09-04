# Decision Report

- generated_at: 2026-09-04T23:36:16.241940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13675**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=13675, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.57% | **+0.32%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.95% | **+0.72%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.50% | **+0.45%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5224件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.73** / 初期 $100.00 (+84.73%)
- 確定: 2426件 (Win 682 / Loss 578 / Flat 1166) / skip 4660件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0537 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $184.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2310件 (Win 687 / Loss 886 / Flat 737) / pending 3件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-04T23:36:06.334387+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79637.7
- Funnel: target 1050 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +36.05% | $9,797,591.85 |
| BASECAT/USDT:USDT | +21.14% | $1,987,449.99 |
| DASH/USDT:USDT | +19.62% | $26,263,914.68 |
| USELESS/USDT:USDT | +17.98% | $44,854,681.40 |
| ZEN/USDT:USDT | +15.05% | $6,312,923.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.61% | +4.56% |
| USELESS/USDT:USDT | below_1h_threshold | +4.49% | +4.44% |
| DASH/USDT:USDT | below_1h_threshold | +4.39% | +4.35% |
| NEAR/USDT:USDT | below_1h_threshold | +2.63% | +2.58% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.89% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
