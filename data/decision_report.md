# Decision Report

- generated_at: 2026-05-28T16:04:33.300469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4972**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=4972, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.58% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.82% | **+1.59%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.31% | **+0.46%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 707件 (Win 174 / Loss 221 / Flat 312) / skip 826件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T16:04:31.012752+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=72785.1
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +4.01% | $5,687,889.38 |
| SWARMS/USDT:USDT | +2.44% | $1,060,980.48 |
| H/USDT:USDT | +0.75% | $6,532,932.52 |
| LYN/USDT:USDT | +0.58% | $1,985,251.09 |
| LIT/USDT:USDT | +0.55% | $1,264,829.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.02% | +4.17% |
| SWARMS/USDT:USDT | below_1h_threshold | +2.90% | +3.06% |
| H/USDT:USDT | below_1h_threshold | +0.75% | +0.91% |
| LYN/USDT:USDT | below_1h_threshold | +0.59% | +0.74% |
| LIT/USDT:USDT | below_1h_threshold | +0.55% | +0.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
