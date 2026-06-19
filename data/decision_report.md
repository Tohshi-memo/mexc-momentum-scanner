# Decision Report

- generated_at: 2026-06-19T16:26:08.566564+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7152**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=7152, expectancy=-0.05%
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
| LIMIT_1PCT | 16/20 | 80.0% | +0.60% | **+0.48%** |
| LIMIT_BB3S | 2/18 | 11.1% | +3.17% | **+0.35%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.18% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.09% | **+0.77%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.47** / 初期 $100.00 (+2.47%)
- 確定トレード: 22件 (TP 9 / SL 13 / EXP 0)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.64% 残高後 $102.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.11** / 初期 $100.00 (+127.11%)
- 確定: 1968件 (Win 571 / Loss 639 / Flat 758) / skip 1745件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 254件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T16:26:02.898901+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=63291.8
- Funnel: target 795 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +14.48% | $2,405,470.31 |
| MYX/USDT:USDT | +5.20% | $2,710,714.45 |
| HEI/USDT:USDT | +5.11% | $13,875,025.29 |
| HIGH/USDT:USDT | +3.64% | $2,530,426.91 |
| BEAT/USDT:USDT | +2.99% | $65,666,031.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_relative_strength | +5.12% | +4.96% |
| HIGH/USDT:USDT | below_1h_threshold | +3.64% | +3.48% |
| BEAT/USDT:USDT | below_1h_threshold | +2.99% | +2.84% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.63% | +2.47% |
| CLO/USDT:USDT | below_1h_threshold | +2.45% | +2.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
