# Decision Report

- generated_at: 2026-06-19T21:38:31.062004+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=7174, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.23% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.43%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.43%** |
| ASK_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.11** / 初期 $100.00 (+127.11%)
- 確定: 1968件 (Win 571 / Loss 639 / Flat 758) / skip 1767件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 275件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T21:38:26.348291+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=63108.6
- Funnel: target 795 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.4 >= 65=1, 4h RSI 91.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +34.55% | $9,981,283.87 |
| BLESS/USDT:USDT | +18.03% | $4,546,089.13 |
| RE/USDT:USDT | +17.36% | $64,537,997.36 |
| BTW/USDT:USDT | +10.32% | $7,522,811.96 |
| MET/USDT:USDT | +8.00% | $1,288,673.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.19% | +3.36% |
| BR/USDT:USDT | below_1h_threshold | +2.41% | +2.59% |
| RIF/USDT:USDT | below_1h_threshold | +2.33% | +2.50% |
| MET/USDT:USDT | below_1h_threshold | +1.78% | +1.95% |
| GUA/USDT:USDT | below_1h_threshold | +0.98% | +1.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
