# Decision Report

- generated_at: 2026-07-01T11:09:43.711026+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7975**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=7975, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| ASK | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +1.20% | **+0.24%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.61** / 初期 $100.00 (+157.61%)
- 確定: 2374件 (Win 720 / Loss 789 / Flat 865) / skip 2162件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $257.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.00** / 初期 $100.00 (+7.00%)
- 確定: 502件 (Win 128 / Loss 121 / Flat 253) / skip 884件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.00

## 5. Latest Market Context

- 更新: 2026-07-01T11:09:38.364445+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=58637.8
- Funnel: target 825 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +84.57% | $8,982,445.56 |
| M/USDT:USDT | +47.26% | $5,326,322.64 |
| BASED/USDT:USDT | +27.15% | $11,811,239.86 |
| BTW/USDT:USDT | +24.79% | $7,820,153.90 |
| BAS/USDT:USDT | +24.08% | $2,566,140.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TOWNS/USDT:USDT | below_1h_threshold | +1.42% | +1.41% |
| NES/USDT:USDT | below_1h_threshold | +1.39% | +1.38% |
| O/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +1.17% | +1.16% |
| ZBT/USDT:USDT | below_1h_threshold | +0.99% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
