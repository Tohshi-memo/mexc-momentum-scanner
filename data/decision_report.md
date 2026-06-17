# Decision Report

- generated_at: 2026-06-17T07:31:37.323483+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6912**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6912, expectancy=-0.06%
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
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.54% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.03% | **+2.27%** |
| ASK_LONG | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.82** / 初期 $100.00 (+98.82%)
- 確定: 1785件 (Win 483 / Loss 557 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $198.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定: 185件 (Win 42 / Loss 35 / Flat 108) / skip 138件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1137 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $101.62

## 5. Latest Market Context

- 更新: 2026-06-17T07:31:32.169854+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=65516.5
- Funnel: target 784 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +33.96% | $4,367,950.67 |
| SQD/USDT:USDT | +28.69% | $2,168,066.76 |
| SPX/USDT:USDT | +22.02% | $8,160,310.34 |
| UNI/USDT:USDT | +20.98% | $50,590,652.07 |
| ROAM/USDT:USDT | +18.43% | $3,293,985.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.63% | +3.75% |
| TRIA/USDT:USDT | below_1h_threshold | +2.17% | +2.28% |
| SPX/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| SPACE/USDT:USDT | below_1h_threshold | +0.86% | +0.97% |
| BR/USDT:USDT | below_1h_threshold | +0.76% | +0.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
