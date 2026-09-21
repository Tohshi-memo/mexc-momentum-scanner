# Decision Report

- generated_at: 2026-09-21T10:11:33.403645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15247**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=15247, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.50% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.61% | **+2.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.53% | **+0.46%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.36% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.55** / 初期 $100.00 (+1073.55%)
- 確定: 5738件 (Win 1709 / Loss 1846 / Flat 2183) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZETA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,173.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.33** / 初期 $100.00 (+147.33%)
- 確定: 3309件 (Win 914 / Loss 765 / Flat 1630) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0151 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3025件 (Win 891 / Loss 1186 / Flat 948) / pending 5件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-21T10:11:17.667363+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=84587.9
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.8 >= 65=1, 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +69.94% | $6,170,458.05 |
| PHA/USDT:USDT | +59.02% | $1,584,925.72 |
| NIL/USDT:USDT | +32.69% | $7,358,542.38 |
| PTB/USDT:USDT | +29.82% | $1,151,631.18 |
| UAI/USDT:USDT | +24.73% | $1,605,209.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.39% | +3.43% |
| ARB/USDT:USDT | below_1h_threshold | +2.54% | +2.59% |
| ENA/USDT:USDT | below_1h_threshold | +2.15% | +2.19% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.08% | +2.12% |
| MINA/USDT:USDT | below_1h_threshold | +1.32% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
