# Decision Report

- generated_at: 2026-07-04T17:42:04.544573+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8280**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=8280, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.48% | **+0.15%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.06% | **+0.04%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.07% | **-0.01%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.22% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$103.12** / 初期 $100.00 (+3.12%)
- 確定トレード: 58件 (TP 21 / SL 36 / EXP 1)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.55** / 初期 $100.00 (+228.55%)
- 確定: 2597件 (Win 823 / Loss 870 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $328.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1054件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T17:41:52.739013+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=63124.3
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +18.53% | $1,735,333.73 |
| RPL/USDT:USDT | +12.98% | $1,075,383.67 |
| SKYAI/USDT:USDT | +8.66% | $9,743,017.14 |
| VELVET/USDT:USDT | +7.12% | $38,219,070.86 |
| BSB/USDT:USDT | +4.42% | $3,518,567.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.13% | +2.76% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.15% | +1.78% |
| BSB/USDT:USDT | below_1h_threshold | +1.78% | +1.42% |
| ICP/USDT:USDT | below_1h_threshold | +1.64% | +1.27% |
| MANA/USDT:USDT | below_1h_threshold | +1.26% | +0.90% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
