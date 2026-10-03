# Decision Report

- generated_at: 2026-10-03T22:11:21.927467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16075**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=16075, expectancy=+0.00%
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
| LIMIT_BB3S | 6/13 | 46.2% | +1.23% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.35% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.74% | **+0.71%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.62% | **+0.19%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +0.28% | **+0.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.02%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.05% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6146件 (Win 1812 / Loss 1972 / Flat 2362) / skip 6490件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3607件 (Win 1005 / Loss 845 / Flat 1757) / skip 5879件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0170 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4235件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000193 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T22:11:10.715956+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=84715.3
- Funnel: target 1086 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +32.08% | $1,091,672.95 |
| SPORTFUN/USDT:USDT | +12.09% | $1,383,942.18 |
| PUMPFUN/USDT:USDT | +10.15% | $41,541,636.38 |
| AKE/USDT:USDT | +9.05% | $3,652,273.04 |
| MOVR/USDT:USDT | +7.90% | $7,094,814.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +1.72% | +1.67% |
| AKE/USDT:USDT | below_1h_threshold | +1.03% | +0.98% |
| STRK/USDT:USDT | below_1h_threshold | +0.89% | +0.83% |
| LINK/USDT:USDT | below_1h_threshold | +0.73% | +0.67% |
| QNT/USDT:USDT | below_1h_threshold | +0.65% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
