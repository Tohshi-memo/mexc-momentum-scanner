# Decision Report

- generated_at: 2026-09-23T17:06:18.397032+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15439**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.59% / filled 20/20。**
- 全期間 MARKET基準: n=15439, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.59% | **+2.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +3.59% | **+2.87%** |
| MARKET | 20/20 | 100.0% | +2.59% | **+2.59%** |
| LIMIT_3PCT | 14/20 | 70.0% | +3.39% | **+2.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.41% | **+2.17%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.83% | **+1.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +1.73% | **+1.13%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.40% | **-0.24%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.67% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5896件 (Win 1739 / Loss 1890 / Flat 2267) / skip 6104件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.67** / 初期 $100.00 (+150.67%)
- 確定: 3386件 (Win 932 / Loss 790 / Flat 1664) / skip 5464件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0487 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $250.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3773件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T17:06:09.176201+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=83826.8
- Funnel: target 1061 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +13.18% | $3,504,055.58 |
| DRIFT/USDT:USDT | +5.17% | $1,945,315.01 |
| FIGHT/USDT:USDT | +4.75% | $1,159,313.30 |
| TAKE/USDT:USDT | +4.58% | $11,899,499.04 |
| RAY/USDT:USDT | +4.32% | $5,600,560.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +1.54% | +1.75% |
| SOXS/USDT:USDT | below_1h_threshold | +0.96% | +1.17% |
| NEMSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +1.13% |
| AKE/USDT:USDT | below_1h_threshold | +0.78% | +0.98% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.71% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
