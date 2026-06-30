# Decision Report

- generated_at: 2026-06-30T03:30:52.632401+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7855**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=7855, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| ASK | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.02% | **+0.02%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.50% | **+0.15%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.10% | **-0.08%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.17% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.44** / 初期 $100.00 (+160.44%)
- 確定: 2353件 (Win 714 / Loss 784 / Flat 855) / skip 2063件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $260.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 809件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T03:30:47.377090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=59816.1
- Funnel: target 811 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1, 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +65.16% | $4,955,577.25 |
| M/USDT:USDT | +28.00% | $2,848,514.18 |
| ANSEM/USDT:USDT | +21.23% | $1,075,750.69 |
| BAS/USDT:USDT | +20.44% | $3,507,043.93 |
| AVAVSTOCK/USDT:USDT | +17.51% | $1,868,753.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +4.73% | +4.90% |
| MYX/USDT:USDT | below_1h_threshold | +2.60% | +2.77% |
| SYN/USDT:USDT | below_1h_threshold | +2.42% | +2.60% |
| XLM/USDT:USDT | below_1h_threshold | +1.82% | +2.00% |
| BILL/USDT:USDT | below_1h_threshold | +1.74% | +1.92% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
