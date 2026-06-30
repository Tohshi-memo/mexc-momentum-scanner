# Decision Report

- generated_at: 2026-06-30T08:52:25.278771+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7875**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=7875, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK | 20/20 | 100.0% | +2.56% | **+2.56%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.63% | **+0.38%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.18% | **-0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$259.13** / 初期 $100.00 (+159.13%)
- 確定: 2354件 (Win 714 / Loss 785 / Flat 855) / skip 2082件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $259.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 829件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T08:52:20.365735+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=59235.4
- Funnel: target 813 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +38.90% | $5,737,047.97 |
| AIGENSYN/USDT:USDT | +37.10% | $10,133,076.02 |
| SYN/USDT:USDT | +33.83% | $28,617,759.07 |
| M/USDT:USDT | +22.94% | $3,761,302.19 |
| AVAVSTOCK/USDT:USDT | +16.59% | $2,102,501.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.54% | +4.98% |
| HEI/USDT:USDT | below_1h_threshold | +4.02% | +4.46% |
| CAP/USDT:USDT | below_1h_threshold | +3.75% | +4.20% |
| BEAT/USDT:USDT | below_1h_threshold | +2.67% | +3.11% |
| BASED/USDT:USDT | below_1h_threshold | +2.63% | +3.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
