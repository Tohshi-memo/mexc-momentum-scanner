# Decision Report

- generated_at: 2026-07-12T21:31:14.110827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8609**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.95% / filled 20/20。**
- 全期間 MARKET基準: n=8609, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.95% | **+2.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +3.68% | **+3.50%** |
| MARKET | 20/20 | 100.0% | +2.95% | **+2.95%** |
| LIMIT_2PCT | 15/20 | 75.0% | +3.44% | **+2.58%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_BB3S | 4/12 | 33.3% | +1.84% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.71% | **+0.50%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.18% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$101.71** / 初期 $100.00 (+1.71%)
- 確定トレード: 90件 (TP 30 / SL 58 / EXP 2)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -2.19% 残高後 $101.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.81** / 初期 $100.00 (+219.81%)
- 確定: 2786件 (Win 875 / Loss 922 / Flat 989) / skip 2384件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDGE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $319.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1376件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 53件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T21:31:07.838111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64060.2
- Funnel: target 863 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +39.20% | $1,632,161.02 |
| BLAST/USDT:USDT | +8.50% | $1,190,237.06 |
| FHE/USDT:USDT | +7.14% | $2,944,247.25 |
| T/USDT:USDT | +7.13% | $20,679,487.66 |
| PIPPIN/USDT:USDT | +7.02% | $6,656,916.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLAST/USDT:USDT | below_1h_threshold | +4.97% | +5.14% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.83% | +3.00% |
| FHE/USDT:USDT | below_1h_threshold | +1.60% | +1.77% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.17% | +1.34% |
| BILL/USDT:USDT | below_1h_threshold | +0.99% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
