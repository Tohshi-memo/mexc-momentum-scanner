# Decision Report

- generated_at: 2026-09-24T05:56:24.215092+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15462**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=15462, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.62% | **+1.53%** |
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
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6125件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.57** / 初期 $100.00 (+152.57%)
- 確定: 3409件 (Win 939 / Loss 791 / Flat 1679) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0728 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.50** / 初期 $100.00 (+21.50%)
- 確定: 3152件 (Win 930 / Loss 1241 / Flat 981) / pending 4件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.50

## 6. Latest Market Context

- 更新: 2026-09-24T05:56:10.250844+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=84101.8
- Funnel: target 1066 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +58.76% | $2,608,520.99 |
| NIL/USDT:USDT | +42.69% | $18,416,032.94 |
| LSK/USDT:USDT | +23.33% | $6,638,120.42 |
| CHR/USDT:USDT | +16.12% | $1,345,573.14 |
| BTW/USDT:USDT | +14.00% | $4,780,033.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.31% | +3.19% |
| LSK/USDT:USDT | below_1h_threshold | +2.78% | +2.66% |
| RAY/USDT:USDT | below_1h_threshold | +2.76% | +2.64% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.55% | +1.43% |
| CRV/USDT:USDT | below_1h_threshold | +1.29% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
