# Decision Report

- generated_at: 2026-11-22T09:06:21.405128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19371**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=19371, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/19 | 57.9% | +2.64% | **+1.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.79% | **+1.07%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.47% | **+0.88%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.41% | **+0.57%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,776.95** / 初期 $100.00 (+1676.95%)
- 確定: 7482件 (Win 2149 / Loss 2409 / Flat 2924) / skip 8450件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.06% 残高後 $1,776.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$451.15** / 初期 $100.00 (+351.15%)
- 確定: 5135件 (Win 1366 / Loss 1104 / Flat 2665) / skip 7647件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0657 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $451.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7530件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000385 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T09:06:09.721585+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=59750.0
- Funnel: target 1086 → liquid 104 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +51.86% | $2,410,569.62 |
| PIEVERSE/USDT:USDT | +42.63% | $10,155,181.33 |
| BLESS/USDT:USDT | +25.91% | $52,603,268.95 |
| BTW/USDT:USDT | +12.06% | $5,372,983.56 |
| VVV/USDT:USDT | +8.53% | $8,084,463.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.23% | +3.28% |
| MMT/USDT:USDT | below_1h_threshold | +2.57% | +2.61% |
| MUU/USDT:USDT | below_1h_threshold | +2.19% | +2.23% |
| KORU/USDT:USDT | below_1h_threshold | +2.05% | +2.09% |
| BLESS/USDT:USDT | below_1h_threshold | +1.73% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
