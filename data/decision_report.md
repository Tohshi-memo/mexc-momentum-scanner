# Decision Report

- generated_at: 2026-06-19T07:26:30.410586+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7111**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=7111, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.13% | **+0.28%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.35% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$103.50** / 初期 $100.00 (+3.50%)
- 確定トレード: 20件 (TP 9 / SL 11 / EXP 0)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.62** / 初期 $100.00 (+121.62%)
- 確定: 1931件 (Win 551 / Loss 622 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $221.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 213件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0574 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T07:26:26.064650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=62793.7
- Funnel: target 795 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +77.47% | $7,492,199.65 |
| HEI/USDT:USDT | +46.88% | $3,031,474.21 |
| ZEREBRO/USDT:USDT | +18.13% | $3,817,479.20 |
| BTW/USDT:USDT | +16.49% | $3,166,217.71 |
| BASED/USDT:USDT | +16.07% | $6,663,612.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.91% | +5.02% |
| BLESS/USDT:USDT | below_1h_threshold | +4.85% | +4.96% |
| BTW/USDT:USDT | below_1h_threshold | +3.95% | +4.06% |
| HEI/USDT:USDT | below_1h_threshold | +2.74% | +2.85% |
| VELVET/USDT:USDT | below_1h_threshold | +2.28% | +2.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
