# Decision Report

- generated_at: 2026-09-19T23:16:09.173346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15106**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=15106, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.59% | **+1.51%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.52% | **+1.29%** |
| LIMIT_BB3S | 7/18 | 38.9% | +3.00% | **+1.17%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.68% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.10% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.04% | **-0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.89% | **-0.29%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.76% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6027件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.24** / 初期 $100.00 (+144.24%)
- 確定: 3219件 (Win 891 / Loss 762 / Flat 1566) / skip 5298件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0263 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CELR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $244.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.80** / 初期 $100.00 (+21.80%)
- 確定: 2976件 (Win 880 / Loss 1177 / Flat 919) / pending 2件 / skip 3601件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.80

## 6. Latest Market Context

- 更新: 2026-09-19T23:16:00.635429+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81273.3
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +52.06% | $43,251,570.41 |
| OFC/USDT:USDT | +45.28% | $1,742,666.40 |
| CELR/USDT:USDT | +42.69% | $1,200,428.48 |
| BANK/USDT:USDT | +17.11% | $2,501,992.32 |
| EVAA/USDT:USDT | +13.58% | $1,183,814.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| G/USDT:USDT | below_1h_threshold | +3.61% | +3.56% |
| EVAA/USDT:USDT | below_1h_threshold | +2.47% | +2.41% |
| ENA/USDT:USDT | below_1h_threshold | +1.95% | +1.90% |
| S/USDT:USDT | below_1h_threshold | +1.66% | +1.61% |
| STX/USDT:USDT | below_1h_threshold | +1.55% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
