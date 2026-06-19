# Decision Report

- generated_at: 2026-06-19T05:23:30.264977+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7102**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7102, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.08% | **-0.05%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_ATR | 9/20 | 45.0% | -0.43% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.97% | **+0.60%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.38% | **+0.35%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.84% | **+0.34%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.64** / 初期 $100.00 (+121.64%)
- 確定: 1922件 (Win 549 / Loss 619 / Flat 754) / skip 1741件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $221.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 205件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T05:23:24.279631+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=62554.7
- Funnel: target 795 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +80.54% | $6,992,947.80 |
| HEI/USDT:USDT | +19.93% | $1,485,444.91 |
| ZEREBRO/USDT:USDT | +19.49% | $3,656,852.23 |
| BASED/USDT:USDT | +15.52% | $5,881,916.66 |
| BTW/USDT:USDT | +15.26% | $3,404,994.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.00% | +3.78% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.42% | +2.21% |
| BASED/USDT:USDT | below_1h_threshold | +1.91% | +1.70% |
| EDEN/USDT:USDT | below_1h_threshold | +1.59% | +1.38% |
| PLAY/USDT:USDT | below_1h_threshold | +1.29% | +1.08% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
