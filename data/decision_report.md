# Decision Report

- generated_at: 2026-06-19T04:29:22.799980+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7098, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.10% | **-0.08%** |
| LIMIT_BB3S | 2/16 | 12.5% | -1.50% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.78% | **+0.55%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.56% | **+0.51%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.15** / 初期 $100.00 (+122.15%)
- 確定: 1918件 (Win 548 / Loss 617 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $222.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 201件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T04:29:17.180803+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62708.6
- Funnel: target 795 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +77.01% | $6,595,856.18 |
| BASED/USDT:USDT | +33.34% | $5,278,697.37 |
| ZEREBRO/USDT:USDT | +22.27% | $3,590,108.15 |
| HEI/USDT:USDT | +13.36% | $1,334,887.58 |
| EDEN/USDT:USDT | +12.80% | $2,388,389.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.21% | +4.27% |
| BEAT/USDT:USDT | below_1h_threshold | +2.39% | +2.45% |
| HEI/USDT:USDT | below_1h_threshold | +2.18% | +2.24% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.53% |
| TAC/USDT:USDT | below_1h_threshold | +0.88% | +0.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
