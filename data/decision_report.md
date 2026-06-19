# Decision Report

- generated_at: 2026-06-19T16:19:04.550027+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7151**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=7151, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.09% | **+0.77%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$102.47** / 初期 $100.00 (+2.47%)
- 確定トレード: 22件 (TP 9 / SL 13 / EXP 0)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.64% 残高後 $102.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.11** / 初期 $100.00 (+127.11%)
- 確定: 1968件 (Win 571 / Loss 639 / Flat 758) / skip 1744件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 253件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T16:18:58.873807+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63252.6
- Funnel: target 795 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +10.95% | $2,160,473.95 |
| MYX/USDT:USDT | +7.01% | $2,618,265.95 |
| HIGH/USDT:USDT | +3.71% | $2,521,427.87 |
| HEI/USDT:USDT | +3.13% | $13,802,551.15 |
| XPL/USDT:USDT | +2.54% | $9,832,518.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +3.71% | +3.62% |
| HEI/USDT:USDT | below_1h_threshold | +3.22% | +3.13% |
| XPL/USDT:USDT | below_1h_threshold | +2.41% | +2.31% |
| ORDI/USDT:USDT | below_1h_threshold | +1.92% | +1.83% |
| RAVE/USDT:USDT | below_1h_threshold | +1.78% | +1.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
