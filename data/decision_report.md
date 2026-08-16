# Decision Report

- generated_at: 2026-08-16T03:06:21.176834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11712**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=11712, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +2.62% | **+2.36%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.82% | **+1.97%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.77% | **+1.68%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.29% | **+1.61%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.93% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.65% | **+0.36%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$633.58** / 初期 $100.00 (+533.58%)
- 確定: 4178件 (Win 1292 / Loss 1358 / Flat 1528) / skip 4095件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $633.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.82** / 初期 $100.00 (+54.82%)
- 確定: 1766件 (Win 493 / Loss 415 / Flat 858) / skip 3357件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0511 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1556件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000073 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T03:06:14.401617+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63091.7
- Funnel: target 985 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +19.89% | $4,926,542.12 |
| SPORTFUN/USDT:USDT | +19.14% | $4,238,764.34 |
| CROSS/USDT:USDT | +13.21% | $1,176,679.54 |
| H/USDT:USDT | +12.77% | $6,333,198.83 |
| AIO/USDT:USDT | +10.73% | $2,651,897.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOS/USDT:USDT | below_1h_threshold | +1.38% | +1.38% |
| CAP/USDT:USDT | below_1h_threshold | +1.05% | +1.05% |
| PRL/USDT:USDT | below_1h_threshold | +0.92% | +0.93% |
| BOME/USDT:USDT | below_1h_threshold | +0.81% | +0.82% |
| SNXX/USDT:USDT | below_1h_threshold | +0.61% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
