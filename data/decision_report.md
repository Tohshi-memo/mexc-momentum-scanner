# Decision Report

- generated_at: 2026-06-24T16:19:12.070108+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7485**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=7485, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.06% | **+2.06%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.92% | **+0.73%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.17% | **-0.08%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.75% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.09** / 初期 $100.00 (+127.09%)
- 確定: 2116件 (Win 626 / Loss 705 / Flat 785) / skip 1930件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 345件 (Win 98 / Loss 95 / Flat 152) / skip 551件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T16:19:06.382769+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=60483.1
- Funnel: target 808 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +6.20% | $16,395,704.31 |
| O/USDT:USDT | +5.25% | $7,055,704.72 |
| BASED/USDT:USDT | +2.66% | $2,716,715.43 |
| ARX/USDT:USDT | +2.64% | $3,657,877.40 |
| SEI/USDT:USDT | +2.27% | $10,325,994.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_relative_strength | +5.30% | +4.93% |
| BASED/USDT:USDT | below_1h_threshold | +2.69% | +2.31% |
| ARX/USDT:USDT | below_1h_threshold | +2.65% | +2.27% |
| SEI/USDT:USDT | below_1h_threshold | +2.27% | +1.90% |
| H/USDT:USDT | below_1h_threshold | +2.27% | +1.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
