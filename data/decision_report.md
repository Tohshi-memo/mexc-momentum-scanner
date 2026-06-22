# Decision Report

- generated_at: 2026-06-22T14:31:21.732614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7375**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=7375, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.60% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.60% | **+0.92%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.34% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.42% | **+0.28%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.32% | **-0.21%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.31% | **-0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.83% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.59** / 初期 $100.00 (+130.59%)
- 確定: 2034件 (Win 600 / Loss 669 / Flat 765) / skip 1902件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $230.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 474件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T14:31:15.002955+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.04% price=64866.0
- Funnel: target 808 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +64.46% | $20,951,544.54 |
| BEL/USDT:USDT | +37.67% | $2,553,547.15 |
| BTW/USDT:USDT | +28.37% | $35,893,066.24 |
| CLO/USDT:USDT | +25.60% | $3,329,701.87 |
| BLESS/USDT:USDT | +18.45% | $2,434,259.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +3.14% | +4.18% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.42% | +2.47% |
| LAYER/USDT:USDT | below_1h_threshold | +0.93% | +1.97% |
| EVAA/USDT:USDT | below_1h_threshold | +0.82% | +1.86% |
| TESLA/USDT:USDT | below_1h_threshold | +0.72% | +1.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
