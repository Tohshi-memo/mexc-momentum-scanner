# Decision Report

- generated_at: 2026-09-22T16:56:45.964772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15341**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=15341, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.55% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.73% | **+0.18%** |
| LIMIT_5PCT | 2/20 | 10.0% | +1.16% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.26% | **+0.84%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.51% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.04% | **+0.04%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.58** / 初期 $100.00 (+1067.58%)
- 確定: 5827件 (Win 1727 / Loss 1875 / Flat 2225) / skip 6075件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,167.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5399件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.97** / 初期 $100.00 (+22.97%)
- 確定: 3106件 (Win 912 / Loss 1216 / Flat 978) / pending 6件 / skip 3713件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.97

## 6. Latest Market Context

- 更新: 2026-09-22T16:56:27.850890+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=86500.3
- Funnel: target 1058 → liquid 187 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.4 >= 65=1, 4h RSI 90.2 >= 65=1, 4h RSI 80.3 >= 65=1, 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUBARAK/USDT:USDT | +18.67% | $10,074,802.40 |
| CHR/USDT:USDT | +15.41% | $2,013,508.70 |
| BR/USDT:USDT | +11.47% | $5,248,216.94 |
| ZRO/USDT:USDT | +8.66% | $3,781,315.04 |
| 4STOCK/USDT:USDT | +5.91% | $4,289,891.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +4.05% | +3.90% |
| SAGA/USDT:USDT | below_1h_threshold | +3.52% | +3.36% |
| GRASS/USDT:USDT | below_1h_threshold | +3.48% | +3.33% |
| DASH/USDT:USDT | below_1h_threshold | +2.90% | +2.75% |
| STRK/USDT:USDT | below_1h_threshold | +2.77% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
