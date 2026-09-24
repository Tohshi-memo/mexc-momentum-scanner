# Decision Report

- generated_at: 2026-09-24T06:16:18.255981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15463**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=15463, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.56% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.39% | **+1.79%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.97% | **+1.48%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.88% | **+1.29%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.70% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6126件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.74** / 初期 $100.00 (+152.74%)
- 確定: 3410件 (Win 940 / Loss 791 / Flat 1679) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0754 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CHR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.28** / 初期 $100.00 (+21.28%)
- 確定: 3153件 (Win 930 / Loss 1242 / Flat 981) / pending 3件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.28

## 6. Latest Market Context

- 更新: 2026-09-24T06:16:07.169137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=84097.3
- Funnel: target 1066 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +59.18% | $2,870,201.73 |
| NIL/USDT:USDT | +30.88% | $18,452,821.09 |
| LSK/USDT:USDT | +26.65% | $6,742,150.30 |
| BTW/USDT:USDT | +14.54% | $4,705,651.19 |
| CHR/USDT:USDT | +13.56% | $1,316,739.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +3.48% | +3.29% |
| PENGU/USDT:USDT | below_1h_threshold | +1.06% | +0.87% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.95% | +0.77% |
| ONDO/USDT:USDT | below_1h_threshold | +0.93% | +0.75% |
| TIA/USDT:USDT | below_1h_threshold | +0.93% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
