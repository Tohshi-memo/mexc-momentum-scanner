# Decision Report

- generated_at: 2026-06-30T11:36:33.709495+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7883, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.02% | **+0.81%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.09% | **+0.66%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.53% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$259.13** / 初期 $100.00 (+159.13%)
- 確定: 2354件 (Win 714 / Loss 785 / Flat 855) / skip 2090件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $259.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 837件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T11:36:23.232493+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=59162.9
- Funnel: target 813 → liquid 149 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +47.70% | $36,509,613.28 |
| BTW/USDT:USDT | +43.15% | $7,763,923.56 |
| AIGENSYN/USDT:USDT | +40.20% | $12,429,120.26 |
| AVAVSTOCK/USDT:USDT | +29.81% | $1,926,138.46 |
| CAP/USDT:USDT | +19.62% | $3,916,887.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.88% | +5.12% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.85% | +5.09% |
| SYN/USDT:USDT | below_1h_threshold | +4.71% | +4.95% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +4.71% | +4.95% |
| BASED/USDT:USDT | below_1h_threshold | +4.06% | +4.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
