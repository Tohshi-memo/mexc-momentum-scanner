# Decision Report

- generated_at: 2026-09-02T11:11:18.161919+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13329**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=13329, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/18 | 50.0% | +1.65% | **+0.83%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.77% | **+0.58%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.05% | **+0.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.56% | **+0.50%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$823.53** / 初期 $100.00 (+723.53%)
- 確定: 4955件 (Win 1503 / Loss 1628 / Flat 1824) / skip 4935件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $823.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.47** / 初期 $100.00 (+75.47%)
- 確定: 2308件 (Win 642 / Loss 552 / Flat 1114) / skip 4432件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: T/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $175.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2705件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T11:11:08.731353+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76619.6
- Funnel: target 1044 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +46.54% | $9,417,305.59 |
| T/USDT:USDT | +41.05% | $4,012,103.23 |
| FONE/USDT:USDT | +32.70% | $1,814,203.58 |
| CASHCAT/USDT:USDT | +19.14% | $1,833,473.25 |
| UAI/USDT:USDT | +14.64% | $26,917,340.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +4.60% | +4.63% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.67% | +1.69% |
| FONE/USDT:USDT | below_1h_threshold | +1.45% | +1.47% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.80% | +0.83% |
| KITE/USDT:USDT | below_1h_threshold | +0.61% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
