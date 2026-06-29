# Decision Report

- generated_at: 2026-06-29T20:12:47.058832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7836**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.42% / filled 20/20。**
- 全期間 MARKET基準: n=7836, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.01% | **+0.75%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.41% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.15% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 44件 (TP 16 / SL 27 / EXP 1)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 2340件 (Win 711 / Loss 779 / Flat 850) / skip 2057件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $263.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 790件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0330 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T20:12:40.164244+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=60427.9
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +13.41% | $14,712,830.99 |
| BAS/USDT:USDT | +9.80% | $2,172,409.01 |
| UB/USDT:USDT | +8.20% | $3,398,358.85 |
| ACT/USDT:USDT | +8.16% | $4,092,972.02 |
| BILL/USDT:USDT | +8.11% | $1,650,178.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACT/USDT:USDT | below_1h_threshold | +2.53% | +2.50% |
| XPL/USDT:USDT | below_1h_threshold | +1.10% | +1.08% |
| BILL/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |
| NES/USDT:USDT | below_1h_threshold | +0.92% | +0.89% |
| M/USDT:USDT | below_1h_threshold | +0.80% | +0.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
