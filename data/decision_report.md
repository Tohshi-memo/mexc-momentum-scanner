# Decision Report

- generated_at: 2026-09-19T00:41:27.266342+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14968**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=14968, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.80% | **+0.68%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.13% | **+0.09%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.65% | **+0.55%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.67% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.32** / 初期 $100.00 (+1095.32%)
- 確定: 5623件 (Win 1687 / Loss 1822 / Flat 2114) / skip 5906件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.82** / 初期 $100.00 (+140.82%)
- 確定: 3174件 (Win 878 / Loss 758 / Flat 1538) / skip 5205件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1292 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $240.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3480件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T00:41:14.243939+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=81246.7
- Funnel: target 1050 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +82.25% | $34,757,822.80 |
| 4/USDT:USDT | +23.12% | $1,270,695.30 |
| SYN/USDT:USDT | +23.02% | $6,816,954.64 |
| MAGMA/USDT:USDT | +22.47% | $1,201,192.71 |
| SAGA/USDT:USDT | +21.55% | $4,198,864.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +4.42% | +3.95% |
| APT/USDT:USDT | below_1h_threshold | +3.59% | +3.12% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.07% | +2.60% |
| AAVE/USDT:USDT | below_1h_threshold | +3.06% | +2.59% |
| SYN/USDT:USDT | below_1h_threshold | +2.73% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
