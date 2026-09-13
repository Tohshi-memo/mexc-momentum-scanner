# Decision Report

- generated_at: 2026-09-13T02:36:47.921653+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14351**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=14351, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.89% | **+1.89%** |
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.88% | **+0.71%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.08% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.49%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.37% | **+1.19%** |
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +2.15% | **+1.08%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.80% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5482件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$218.47** / 初期 $100.00 (+118.47%)
- 確定: 2869件 (Win 795 / Loss 670 / Flat 1404) / skip 4893件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1435 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $218.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.85** / 初期 $100.00 (+25.85%)
- 確定: 2802件 (Win 833 / Loss 1078 / Flat 891) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000420 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.85

## 6. Latest Market Context

- 更新: 2026-09-13T02:36:32.084695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=77242.2
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.2 >= 65=1, 4h RSI 94.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +116.35% | $67,392,898.17 |
| POWR/USDT:USDT | +48.55% | $1,292,593.17 |
| ZCAT/USDT:USDT | +35.57% | $1,134,912.10 |
| STORJ/USDT:USDT | +19.61% | $19,276,274.64 |
| ALCH/USDT:USDT | +17.66% | $2,680,070.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWR/USDT:USDT | below_1h_threshold | +1.76% | +1.82% |
| AKE/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |
| STX/USDT:USDT | below_1h_threshold | +1.29% | +1.35% |
| STORJ/USDT:USDT | below_1h_threshold | +1.11% | +1.17% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
