# Decision Report

- generated_at: 2026-09-12T22:46:14.579319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14327**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14327, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.62% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.63% | **+1.47%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.34% | **+1.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.30% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5459件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$213.42** / 初期 $100.00 (+113.42%)
- 確定: 2845件 (Win 785 / Loss 660 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1471 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $213.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.38** / 初期 $100.00 (+24.38%)
- 確定: 2778件 (Win 823 / Loss 1068 / Flat 887) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000448 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $124.38

## 6. Latest Market Context

- 更新: 2026-09-12T22:46:04.671155+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77157.8
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +20.50% | $22,827,980.82 |
| LONGXIA/USDT:USDT | +18.90% | $9,834,243.28 |
| REZ/USDT:USDT | +15.16% | $1,966,995.82 |
| RIVER/USDT:USDT | +10.32% | $15,303,479.98 |
| LSK/USDT:USDT | +8.13% | $47,197,825.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRIFFAIN/USDT:USDT | below_1h_threshold | +2.21% | +2.29% |
| IOST/USDT:USDT | below_1h_threshold | +1.02% | +1.10% |
| AKE/USDT:USDT | below_1h_threshold | +1.00% | +1.08% |
| REZ/USDT:USDT | below_1h_threshold | +0.59% | +0.67% |
| SOXS/USDT:USDT | below_1h_threshold | +0.25% | +0.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
