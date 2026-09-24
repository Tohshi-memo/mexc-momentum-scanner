# Decision Report

- generated_at: 2026-09-24T01:11:33.610960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15454**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=15454, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.43% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.16% | **+1.19%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.88% | **+1.03%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6118件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.21** / 初期 $100.00 (+152.21%)
- 確定: 3401件 (Win 937 / Loss 791 / Flat 1673) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0560 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $252.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.85** / 初期 $100.00 (+20.85%)
- 確定: 3144件 (Win 926 / Loss 1238 / Flat 980) / pending 2件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000267 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $120.85

## 6. Latest Market Context

- 更新: 2026-09-24T01:11:20.521699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=84229.5
- Funnel: target 1061 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +45.09% | $1,487,199.33 |
| NIL/USDT:USDT | +36.31% | $14,076,523.00 |
| LSK/USDT:USDT | +13.85% | $4,540,122.41 |
| BTW/USDT:USDT | +11.11% | $3,947,834.26 |
| UAI/USDT:USDT | +8.08% | $2,418,565.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHR/USDT:USDT | below_1h_threshold | +0.92% | +0.97% |
| LTC/USDT:USDT | below_1h_threshold | +0.77% | +0.83% |
| LAB/USDT:USDT | below_1h_threshold | +0.76% | +0.81% |
| BR/USDT:USDT | below_1h_threshold | +0.61% | +0.67% |
| SYN/USDT:USDT | below_1h_threshold | +0.59% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
