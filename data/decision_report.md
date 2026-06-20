# Decision Report

- generated_at: 2026-06-20T16:45:04.874131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7251**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.96% / filled 20/20。**
- 全期間 MARKET基準: n=7251, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.96% | **+1.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.96% | **+1.96%** |
| ASK | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.19% | **+1.64%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.22% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.93% | **-0.42%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.98% | **-0.49%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.99% | **-0.49%** |
| MARKET_LONG | 20/20 | 100.0% | -0.55% | **-0.55%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.93** / 初期 $100.00 (+125.93%)
- 確定: 1980件 (Win 576 / Loss 646 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 352件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T16:44:56.558473+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=63972.6
- Funnel: target 796 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +8.01% | $12,966,958.57 |
| BICO/USDT:USDT | +7.07% | $33,755,814.57 |
| AGT/USDT:USDT | +4.67% | $2,361,838.03 |
| ASTEROID/USDT:USDT | +3.01% | $1,973,302.98 |
| CHIP/USDT:USDT | +2.67% | $1,141,668.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.91% | +5.16% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.02% | +3.26% |
| CHIP/USDT:USDT | below_1h_threshold | +2.88% | +3.13% |
| LAB/USDT:USDT | below_1h_threshold | +2.86% | +3.10% |
| SYN/USDT:USDT | below_1h_threshold | +2.44% | +2.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
