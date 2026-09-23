# Decision Report

- generated_at: 2026-09-23T12:26:28.279392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15430**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=15430, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +4.38% | **+2.02%** |
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_ATR | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.22% | **+1.55%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.88% | **+1.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +0.56% | **+0.50%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.33% | **+0.18%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6096件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.06** / 初期 $100.00 (+149.06%)
- 確定: 3377件 (Win 931 / Loss 789 / Flat 1657) / skip 5464件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $249.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3766件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T12:26:17.277276+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=85456.2
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMISTOCK/USDT:USDT | +782.67% | $1,591,240.20 |
| TAKE/USDT:USDT | +225.58% | $6,607,300.04 |
| SHROOM/USDT:USDT | +65.87% | $1,398,308.75 |
| MET/USDT:USDT | +36.33% | $1,767,982.05 |
| ALLO/USDT:USDT | +31.14% | $4,657,994.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.06% | +3.25% |
| COTI/USDT:USDT | below_1h_threshold | +2.88% | +3.07% |
| SHROOM/USDT:USDT | below_1h_threshold | +2.49% | +2.68% |
| NIL/USDT:USDT | below_1h_threshold | +2.29% | +2.48% |
| NEAR/USDT:USDT | below_1h_threshold | +2.11% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
