# Decision Report

- generated_at: 2026-09-11T15:31:28.888445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14230**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=14230, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.88% | **+0.24%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.90% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.46% | **+1.11%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.58%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.81% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.25** / 初期 $100.00 (+978.25%)
- 確定: 5389件 (Win 1623 / Loss 1743 / Flat 2023) / skip 5402件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,078.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.79** / 初期 $100.00 (+107.79%)
- 確定: 2807件 (Win 770 / Loss 651 / Flat 1386) / skip 4834件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $207.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.49** / 初期 $100.00 (+23.49%)
- 確定: 2729件 (Win 807 / Loss 1045 / Flat 877) / pending 6件 / skip 2970件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000273 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.49

## 6. Latest Market Context

- 更新: 2026-09-11T15:31:18.915132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78656.1
- Funnel: target 1067 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STONK/USDT:USDT | +79.80% | $1,252,223.73 |
| NIULAI/USDT:USDT | +69.36% | $22,979,290.97 |
| STORJ/USDT:USDT | +60.81% | $5,410,900.49 |
| LAB/USDT:USDT | +25.79% | $3,169,604.58 |
| RAY/USDT:USDT | +24.34% | $25,834,288.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STONK/USDT:USDT | below_1h_threshold | +3.72% | +3.85% |
| CHIP/USDT:USDT | below_1h_threshold | +2.93% | +3.06% |
| LAB/USDT:USDT | below_1h_threshold | +2.91% | +3.04% |
| INJ/USDT:USDT | below_1h_threshold | +2.48% | +2.61% |
| AERO/USDT:USDT | below_1h_threshold | +2.10% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
