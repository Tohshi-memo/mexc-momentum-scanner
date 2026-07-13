# Decision Report

- generated_at: 2026-07-13T12:26:14.075770+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8633**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=8633, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.68% | **+1.51%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.61% | **+0.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.67% | **+0.53%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.24% | **-0.18%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| MARKET_LONG | 20/20 | 100.0% | -0.40% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.69** / 初期 $100.00 (+0.69%)
- 確定トレード: 92件 (TP 30 / SL 60 / EXP 2)
- 最新: TRIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.16** / 初期 $100.00 (+222.16%)
- 確定: 2801件 (Win 878 / Loss 923 / Flat 1000) / skip 2393件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DODO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $322.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1399件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0066 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.31** / 初期 $100.00 (-0.69%)
- 確定: 37件 (Win 13 / Loss 24 / Flat 0) / pending 2件 / skip 63件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000507 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DODO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.31

## 6. Latest Market Context

- 更新: 2026-07-13T12:26:07.806336+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62800.1
- Funnel: target 867 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +32.02% | $10,828,333.53 |
| JCT/USDT:USDT | +28.88% | $1,709,771.72 |
| XEC/USDT:USDT | +26.45% | $5,376,157.83 |
| KITE/USDT:USDT | +20.01% | $3,737,898.20 |
| BILL/USDT:USDT | +12.01% | $14,020,878.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.18% | +3.31% |
| BILL/USDT:USDT | below_1h_threshold | +1.56% | +1.69% |
| ALLO/USDT:USDT | below_1h_threshold | +1.31% | +1.44% |
| VELVET/USDT:USDT | below_1h_threshold | +1.22% | +1.35% |
| JCT/USDT:USDT | below_1h_threshold | +1.12% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
