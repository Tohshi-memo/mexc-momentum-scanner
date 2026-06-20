# Decision Report

- generated_at: 2026-06-20T17:13:57.602028+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7256**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=7256, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| ASK | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.61% | **+0.54%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.58% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.91% | **-0.36%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -1.32% | **-0.60%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.79** / 初期 $100.00 (+132.79%)
- 確定: 1985件 (Win 581 / Loss 646 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $232.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 357件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T17:13:48.773631+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63908.2
- Funnel: target 796 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +27.86% | $34,243,075.99 |
| AGT/USDT:USDT | +11.76% | $2,438,167.77 |
| VELVET/USDT:USDT | +11.45% | $13,002,758.81 |
| LAB/USDT:USDT | +6.53% | $28,607,862.52 |
| RIF/USDT:USDT | +4.49% | $3,304,135.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.41% | +3.55% |
| LAB/USDT:USDT | below_1h_threshold | +2.60% | +2.73% |
| RIF/USDT:USDT | below_1h_threshold | +2.43% | +2.57% |
| SYN/USDT:USDT | below_1h_threshold | +1.55% | +1.69% |
| UB/USDT:USDT | below_1h_threshold | +1.06% | +1.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
