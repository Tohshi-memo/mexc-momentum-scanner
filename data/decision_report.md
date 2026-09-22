# Decision Report

- generated_at: 2026-09-22T22:56:30.566343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15370**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=15370, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.07% | **+1.76%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.31% | **+1.62%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.62% | **+1.44%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_BB3S | 8/14 | 57.1% | +1.72% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.91% | **+1.31%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.42% | **+1.14%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.82** / 初期 $100.00 (+1055.82%)
- 確定: 5848件 (Win 1729 / Loss 1880 / Flat 2239) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,155.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5428件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.29** / 初期 $100.00 (+22.29%)
- 確定: 3118件 (Win 916 / Loss 1223 / Flat 979) / pending 4件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000096 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.29

## 6. Latest Market Context

- 更新: 2026-09-22T22:56:17.215725+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=86133.6
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DRIFT/USDT:USDT | +28.16% | $1,644,526.87 |
| MUSEBOOK/USDT:USDT | +28.07% | $1,042,439.83 |
| FOLKS/USDT:USDT | +25.31% | $2,348,654.68 |
| 4/USDT:USDT | +19.61% | $2,338,356.83 |
| MUBARAK/USDT:USDT | +15.82% | $17,054,768.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +4.01% | +4.03% |
| BTW/USDT:USDT | below_1h_threshold | +3.48% | +3.49% |
| ARB/USDT:USDT | below_1h_threshold | +3.07% | +3.08% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.50% | +2.51% |
| SAGA/USDT:USDT | below_1h_threshold | +2.49% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
