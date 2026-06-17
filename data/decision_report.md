# Decision Report

- generated_at: 2026-06-17T08:03:07.589932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6913**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6913, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.63% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.88% | **+3.53%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.59% | **+2.07%** |
| ASK_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.83** / 初期 $100.00 (+97.83%)
- 確定: 1786件 (Win 483 / Loss 558 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $197.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 186件 (Win 42 / Loss 36 / Flat 108) / skip 138件
- 成長率目線: 平均log +0.000068 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1112 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.27

## 5. Latest Market Context

- 更新: 2026-06-17T08:03:03.367231+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=65430.8
- Funnel: target 784 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +34.90% | $4,482,530.43 |
| SQD/USDT:USDT | +27.71% | $2,248,294.05 |
| ROAM/USDT:USDT | +26.56% | $3,020,970.85 |
| SPX/USDT:USDT | +20.22% | $8,295,757.46 |
| UNI/USDT:USDT | +19.72% | $51,783,722.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +0.66% | +0.77% |
| SQD/USDT:USDT | below_1h_threshold | +0.56% | +0.67% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.59% |
| LIT/USDT:USDT | below_1h_threshold | +0.46% | +0.57% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.44% | +0.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
