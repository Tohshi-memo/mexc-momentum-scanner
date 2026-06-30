# Decision Report

- generated_at: 2026-06-30T11:27:23.599013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7882**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=7882, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.72% | **+0.61%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.42% | **+0.28%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.23% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$259.13** / 初期 $100.00 (+159.13%)
- 確定: 2354件 (Win 714 / Loss 785 / Flat 855) / skip 2089件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $259.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 836件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T11:27:12.973689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=59206.4
- Funnel: target 813 → liquid 149 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +44.48% | $35,642,706.15 |
| BTW/USDT:USDT | +41.68% | $7,597,556.71 |
| AIGENSYN/USDT:USDT | +36.36% | $12,387,550.73 |
| AVAVSTOCK/USDT:USDT | +26.63% | $1,894,356.79 |
| H/USDT:USDT | +17.65% | $9,714,605.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +3.39% | +3.55% |
| SYN/USDT:USDT | below_1h_threshold | +2.65% | +2.81% |
| HEI/USDT:USDT | below_1h_threshold | +2.37% | +2.53% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.98% | +2.14% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
