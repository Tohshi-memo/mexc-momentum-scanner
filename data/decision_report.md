# Decision Report

- generated_at: 2026-10-03T22:21:24.910726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16076**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=16076, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_BB3S | 6/13 | 46.2% | +1.25% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.35% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.68% | **+0.64%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +0.66% | **+0.23%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.05% | **-0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.51% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6146件 (Win 1812 / Loss 1972 / Flat 2362) / skip 6491件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3607件 (Win 1005 / Loss 845 / Flat 1757) / skip 5880件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0156 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4235件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T22:21:13.989747+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=84731.4
- Funnel: target 1086 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +31.36% | $1,100,844.74 |
| SPORTFUN/USDT:USDT | +12.80% | $1,394,477.85 |
| PUMPFUN/USDT:USDT | +10.30% | $41,870,994.64 |
| AKE/USDT:USDT | +8.63% | $3,681,218.47 |
| MONAD/USDT:USDT | +6.11% | $1,749,442.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +0.80% | +0.73% |
| AKE/USDT:USDT | below_1h_threshold | +0.67% | +0.60% |
| STRK/USDT:USDT | below_1h_threshold | +0.52% | +0.45% |
| SKY/USDT:USDT | below_1h_threshold | +0.49% | +0.42% |
| LINK/USDT:USDT | below_1h_threshold | +0.48% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
