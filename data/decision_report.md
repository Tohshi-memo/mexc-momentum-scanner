# Decision Report

- generated_at: 2026-09-19T03:36:17.078230+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14985**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=14985, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.20% | **+1.08%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.14% | **+1.86%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.71% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,201.40** / 初期 $100.00 (+1101.40%)
- 確定: 5638件 (Win 1691 / Loss 1828 / Flat 2119) / skip 5908件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,201.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.14** / 初期 $100.00 (+139.14%)
- 確定: 3178件 (Win 878 / Loss 760 / Flat 1540) / skip 5218件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3496件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T03:36:08.315539+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=81082.5
- Funnel: target 1050 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +63.10% | $38,889,411.71 |
| ONE/USDT:USDT | +36.57% | $26,456,911.21 |
| CATE/USDT:USDT | +28.74% | $1,388,632.12 |
| AR/USDT:USDT | +27.32% | $4,730,224.68 |
| MAGMA/USDT:USDT | +24.39% | $1,263,512.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +3.91% | +4.12% |
| STRK/USDT:USDT | below_1h_threshold | +3.89% | +4.11% |
| CHIP/USDT:USDT | below_1h_threshold | +2.88% | +3.10% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.69% | +1.90% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.66% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
