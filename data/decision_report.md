# Decision Report

- generated_at: 2026-06-19T12:49:54.726684+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7140**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7140, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| ASK_LONG | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.06% | **+1.65%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.04% | **+1.63%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.05** / 初期 $100.00 (+134.05%)
- 確定: 1960件 (Win 570 / Loss 632 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $234.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 242件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T12:49:50.369283+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=62336.8
- Funnel: target 795 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +86.57% | $8,702,387.41 |
| RE/USDT:USDT | +60.59% | $39,064,914.84 |
| HEI/USDT:USDT | +46.31% | $9,485,923.26 |
| BTW/USDT:USDT | +37.69% | $3,824,567.70 |
| ZEREBRO/USDT:USDT | +28.78% | $4,681,216.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.38% | +3.81% |
| RE/USDT:USDT | below_1h_threshold | +3.29% | +3.71% |
| HIGH/USDT:USDT | below_1h_threshold | +3.20% | +3.62% |
| CLO/USDT:USDT | below_1h_threshold | +3.07% | +3.49% |
| BASED/USDT:USDT | below_1h_threshold | +2.94% | +3.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
