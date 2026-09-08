# Decision Report

- generated_at: 2026-09-08T23:56:14.910060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14021**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=14021, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.20% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +0.56% | **+0.25%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.26% | **+0.21%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.51% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5285件 (Win 1588 / Loss 1707 / Flat 1990) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2624件 (Win 726 / Loss 622 / Flat 1276) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.46** / 初期 $100.00 (+19.46%)
- 確定: 2604件 (Win 762 / Loss 990 / Flat 852) / pending 2件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` EXPIRED account -0.02% 残高後 $119.46

## 6. Latest Market Context

- 更新: 2026-09-08T23:56:06.560614+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=78393.7
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +45.06% | $1,023,480.74 |
| ARX/USDT:USDT | +9.73% | $1,145,416.51 |
| RAY/USDT:USDT | +8.99% | $2,980,770.01 |
| EGLD/USDT:USDT | +7.20% | $2,090,450.40 |
| FF/USDT:USDT | +6.47% | $1,983,751.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.42% | +4.59% |
| VVV/USDT:USDT | below_1h_threshold | +3.19% | +3.36% |
| BULLA/USDT:USDT | below_1h_threshold | +2.00% | +2.17% |
| VET/USDT:USDT | below_1h_threshold | +1.98% | +2.15% |
| HNT/USDT:USDT | below_1h_threshold | +1.70% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
