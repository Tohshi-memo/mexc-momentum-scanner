# Decision Report

- generated_at: 2026-06-14T15:42:57.822735+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6676**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.28% / filled 20/20。**
- 全期間 MARKET基準: n=6676, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |
| ASK | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.51% | **+1.29%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.20** / 初期 $100.00 (+71.20%)
- 確定: 1549件 (Win 411 / Loss 491 / Flat 647) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $171.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 61件 (Win 19 / Loss 12 / Flat 30) / skip 26件
- 成長率目線: 平均log -0.000165 / 幾何平均 -0.016% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T15:42:54.166593+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64013.4
- Funnel: target 770 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +41.34% | $99,955,583.11 |
| CLO/USDT:USDT | +25.88% | $1,265,379.04 |
| TRADOOR/USDT:USDT | +24.36% | $9,085,854.12 |
| OPG/USDT:USDT | +23.91% | $1,686,116.62 |
| BANANAS31/USDT:USDT | +23.30% | $1,731,399.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.41% | +4.32% |
| MEGA/USDT:USDT | below_1h_threshold | +4.10% | +4.01% |
| BSB/USDT:USDT | below_1h_threshold | +3.75% | +3.65% |
| NOT/USDT:USDT | below_1h_threshold | +3.30% | +3.20% |
| LIT/USDT:USDT | below_1h_threshold | +2.90% | +2.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
