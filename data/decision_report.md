# Decision Report

- generated_at: 2026-08-18T08:06:21.813059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11889**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=11889, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.22% | **+0.91%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_BB3S | 3/20 | 15.0% | +3.88% | **+0.58%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.79% | **+0.90%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.58% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$612.37** / 初期 $100.00 (+512.37%)
- 確定: 4190件 (Win 1293 / Loss 1367 / Flat 1530) / skip 4260件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $612.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3481件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0055 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.85** / 初期 $100.00 (+16.85%)
- 確定: 1700件 (Win 505 / Loss 645 / Flat 550) / pending 5件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EDEN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.85

## 6. Latest Market Context

- 更新: 2026-08-18T08:06:15.944351+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64127.0
- Funnel: target 992 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +22.54% | $2,862,076.38 |
| RED/USDT:USDT | +14.91% | $2,384,469.38 |
| CYS/USDT:USDT | +14.13% | $17,105,054.86 |
| SOXS/USDT:USDT | +11.50% | $7,018,216.94 |
| OPN/USDT:USDT | +11.41% | $1,035,320.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.82% | +2.89% |
| GPS/USDT:USDT | below_1h_threshold | +1.78% | +1.84% |
| SOXS/USDT:USDT | below_1h_threshold | +1.73% | +1.79% |
| OPN/USDT:USDT | below_1h_threshold | +1.12% | +1.19% |
| PRL/USDT:USDT | below_1h_threshold | +1.09% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
