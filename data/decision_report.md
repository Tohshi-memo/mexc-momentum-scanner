# Decision Report

- generated_at: 2026-09-24T00:21:16.144046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15449**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=15449, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.40% | **+1.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.16% | **+1.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.81% | **+0.48%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6113件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.92** / 初期 $100.00 (+152.92%)
- 確定: 3396件 (Win 936 / Loss 790 / Flat 1670) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0678 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定: 3141件 (Win 925 / Loss 1237 / Flat 979) / pending 1件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $121.01

## 6. Latest Market Context

- 更新: 2026-09-24T00:21:04.683594+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=84389.3
- Funnel: target 1061 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +38.45% | $12,863,358.74 |
| LSK/USDT:USDT | +12.84% | $4,391,750.30 |
| BTW/USDT:USDT | +10.58% | $3,839,725.10 |
| MARSCOIN/USDT:USDT | +7.85% | $3,362,704.59 |
| HNT/USDT:USDT | +7.77% | $1,244,227.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +3.65% | +3.61% |
| COMP/USDT:USDT | below_1h_threshold | +3.44% | +3.40% |
| SYN/USDT:USDT | below_1h_threshold | +2.20% | +2.16% |
| USELESS/USDT:USDT | below_1h_threshold | +1.84% | +1.80% |
| KERNEL/USDT:USDT | below_1h_threshold | +1.84% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
