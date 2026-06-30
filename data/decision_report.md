# Decision Report

- generated_at: 2026-06-30T02:46:07.010354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7850**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=7850, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| ASK | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.54% | **+0.48%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.50% | **+0.15%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.44** / 初期 $100.00 (+160.44%)
- 確定: 2353件 (Win 714 / Loss 784 / Flat 855) / skip 2058件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $260.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 804件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T02:46:01.758305+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=59994.2
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 94.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +38.74% | $1,062,073.95 |
| CAP/USDT:USDT | +27.25% | $2,341,960.03 |
| AIGENSYN/USDT:USDT | +17.76% | $3,941,740.77 |
| M/USDT:USDT | +17.75% | $2,710,381.31 |
| AVAVSTOCK/USDT:USDT | +17.52% | $1,849,665.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.35% | +3.22% |
| NES/USDT:USDT | below_1h_threshold | +1.80% | +1.67% |
| CHZ/USDT:USDT | below_1h_threshold | +1.26% | +1.13% |
| KORU/USDT:USDT | below_1h_threshold | +1.15% | +1.02% |
| LIT/USDT:USDT | below_1h_threshold | +0.90% | +0.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
