# Decision Report

- generated_at: 2026-08-15T13:51:43.544941+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11673**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=11673, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.45% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4141件 (Win 1290 / Loss 1355 / Flat 1496) / skip 4093件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1736件 (Win 492 / Loss 413 / Flat 831) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0960 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.76** / 初期 $100.00 (+19.76%)
- 確定: 1614件 (Win 493 / Loss 611 / Flat 510) / pending 5件 / skip 1527件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000629 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.76

## 6. Latest Market Context

- 更新: 2026-08-15T13:51:28.267360+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63013.7
- Funnel: target 985 → liquid 151 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1, 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +50.50% | $8,027,609.93 |
| WAL/USDT:USDT | +26.46% | $1,485,724.88 |
| VELVET/USDT:USDT | +24.91% | $31,485,712.33 |
| ANSEM/USDT:USDT | +24.49% | $1,705,216.98 |
| CYS/USDT:USDT | +23.90% | $20,437,022.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +3.42% | +3.45% |
| AEON1/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.46% | +1.48% |
| VELVET/USDT:USDT | below_1h_threshold | +1.22% | +1.24% |
| NIL/USDT:USDT | below_1h_threshold | +0.82% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
