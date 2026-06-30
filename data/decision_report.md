# Decision Report

- generated_at: 2026-06-30T04:47:53.576769+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7861**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.34% / filled 20/20。**
- 全期間 MARKET基準: n=7861, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |
| ASK | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_1PCT | 13/20 | 65.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.02% | **-0.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.57% | **-0.32%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.80% | **-0.64%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.44** / 初期 $100.00 (+160.44%)
- 確定: 2353件 (Win 714 / Loss 784 / Flat 855) / skip 2069件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $260.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 815件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T04:47:44.292329+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=59546.5
- Funnel: target 816 → liquid 151 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +51.15% | $6,145,707.28 |
| M/USDT:USDT | +24.70% | $3,368,297.61 |
| ANSEM/USDT:USDT | +22.60% | $1,092,880.84 |
| SYN/USDT:USDT | +18.49% | $22,928,630.86 |
| AVAVSTOCK/USDT:USDT | +17.67% | $1,883,169.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.98% | +4.07% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.89% | +3.97% |
| M/USDT:USDT | below_1h_threshold | +3.39% | +3.48% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.01% | +3.09% |
| NES/USDT:USDT | below_1h_threshold | +2.45% | +2.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
