# Decision Report

- generated_at: 2026-07-12T22:31:11.565093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8611**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=8611, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.52% | **+2.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.48% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.12% | **+0.78%** |
| LIMIT_BB3S | 4/10 | 40.0% | +1.84% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.46% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.71** / 初期 $100.00 (+1.71%)
- 確定トレード: 90件 (TP 30 / SL 58 / EXP 2)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -2.19% 残高後 $101.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.81** / 初期 $100.00 (+219.81%)
- 確定: 2788件 (Win 875 / Loss 922 / Flat 991) / skip 2384件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DODO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $319.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1378件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 55件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T22:31:05.224714+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=63806.9
- Funnel: target 863 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +41.65% | $2,700,390.56 |
| BLAST/USDT:USDT | +17.01% | $1,254,800.27 |
| FHE/USDT:USDT | +5.63% | $3,004,818.01 |
| PIPPIN/USDT:USDT | +5.17% | $7,067,439.99 |
| T/USDT:USDT | +3.83% | $20,878,804.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +2.68% | +2.81% |
| SYN/USDT:USDT | below_1h_threshold | +0.89% | +1.02% |
| EGLD/USDT:USDT | below_1h_threshold | +0.27% | +0.40% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.10% | +0.23% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +0.05% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
