# Decision Report

- generated_at: 2026-06-06T06:00:53.604097+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5787**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.06% / filled 20/20。**
- 全期間 MARKET基準: n=5787, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.06% | **+3.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.10% | **+3.10%** |
| MARKET | 20/20 | 100.0% | +3.06% | **+3.06%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.19% | **+0.82%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.51% | **+0.18%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.45% | **+0.09%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -0.73% | **-0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1336件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T06:00:50.808247+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=61010.4
- Funnel: target 771 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +28.53% | $8,706,986.81 |
| OPN/USDT:USDT | +25.86% | $22,643,749.01 |
| CLO/USDT:USDT | +23.48% | $1,744,859.55 |
| VELVET/USDT:USDT | +23.05% | $2,151,355.36 |
| ZEST/USDT:USDT | +18.15% | $1,705,724.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +0.65% | +0.50% |
| ZEC/USDT:USDT | below_1h_threshold | +0.60% | +0.45% |
| GUA/USDT:USDT | below_1h_threshold | +0.59% | +0.44% |
| NEAR/USDT:USDT | below_1h_threshold | +0.57% | +0.42% |
| ALLO/USDT:USDT | below_1h_threshold | +0.52% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
