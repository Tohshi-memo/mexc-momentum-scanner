# Decision Report

- generated_at: 2026-06-26T00:09:25.280477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7596**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7596, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_5PCT | 2/20 | 10.0% | -1.52% | **-0.15%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.93% | **-0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.37% | **+1.54%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.83% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2025件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 379件 (Win 103 / Loss 100 / Flat 176) / skip 628件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T00:09:18.646025+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=59775.0
- Funnel: target 807 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +31.25% | $1,916,511.56 |
| IP/USDT:USDT | +17.80% | $3,221,017.54 |
| IDOL/USDT:USDT | +17.58% | $1,589,135.22 |
| AIN/USDT:USDT | +17.25% | $1,759,469.90 |
| HEI/USDT:USDT | +12.52% | $6,453,372.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +3.74% | +3.73% |
| IP/USDT:USDT | below_1h_threshold | +2.90% | +2.89% |
| AIN/USDT:USDT | below_1h_threshold | +1.65% | +1.64% |
| SLX/USDT:USDT | below_1h_threshold | +1.64% | +1.63% |
| INJ/USDT:USDT | below_1h_threshold | +1.19% | +1.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
