# Decision Report

- generated_at: 2026-06-19T11:05:35.367940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7126, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.32** / 初期 $100.00 (+128.32%)
- 確定: 1946件 (Win 561 / Loss 627 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $228.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 228件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0508 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T11:05:29.664980+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62530.0
- Funnel: target 795 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +73.03% | $8,277,600.21 |
| HEI/USDT:USDT | +58.64% | $7,800,212.57 |
| RE/USDT:USDT | +33.44% | $24,293,458.93 |
| BTW/USDT:USDT | +31.39% | $3,420,070.81 |
| ZEREBRO/USDT:USDT | +28.24% | $4,233,884.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.45% | +1.41% |
| EDEN/USDT:USDT | below_1h_threshold | +1.08% | +1.04% |
| BEAT/USDT:USDT | below_1h_threshold | +1.02% | +0.99% |
| HEI/USDT:USDT | below_1h_threshold | +0.96% | +0.92% |
| BASED/USDT:USDT | below_1h_threshold | +0.90% | +0.86% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
