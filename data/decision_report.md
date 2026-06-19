# Decision Report

- generated_at: 2026-06-19T02:22:02.565096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7093**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=7093, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.92% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.33% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.03% | **+0.82%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.54% | **+0.52%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.56% | **+0.51%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.06** / 初期 $100.00 (+121.06%)
- 確定: 1913件 (Win 545 / Loss 615 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $221.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 196件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T02:21:58.124096+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62949.9
- Funnel: target 795 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +85.09% | $6,028,556.81 |
| BASED/USDT:USDT | +33.54% | $4,047,674.68 |
| ZEREBRO/USDT:USDT | +18.91% | $3,350,509.53 |
| EDEN/USDT:USDT | +15.03% | $2,169,144.68 |
| LAB/USDT:USDT | +14.45% | $35,154,279.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.77% | +2.84% |
| LAB/USDT:USDT | below_1h_threshold | +2.21% | +2.28% |
| HEI/USDT:USDT | below_1h_threshold | +2.18% | +2.25% |
| ENJ/USDT:USDT | below_1h_threshold | +1.22% | +1.29% |
| IP/USDT:USDT | below_1h_threshold | +1.21% | +1.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
