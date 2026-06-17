# Decision Report

- generated_at: 2026-06-17T08:09:41.046728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6914**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6914, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.03% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.88% | **+3.53%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.23% | **+1.67%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.82** / 初期 $100.00 (+98.82%)
- 確定: 1787件 (Win 484 / Loss 558 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $198.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 187件 (Win 42 / Loss 36 / Flat 109) / skip 138件
- 成長率目線: 平均log +0.000067 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1158 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $101.27

## 5. Latest Market Context

- 更新: 2026-06-17T08:09:35.948888+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=65389.9
- Funnel: target 784 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +37.03% | $4,519,757.58 |
| SQD/USDT:USDT | +28.28% | $2,276,150.97 |
| ROAM/USDT:USDT | +25.37% | $3,032,508.73 |
| SPX/USDT:USDT | +20.94% | $8,334,630.68 |
| UNI/USDT:USDT | +18.83% | $51,920,764.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.55% | +1.72% |
| LIT/USDT:USDT | below_1h_threshold | +1.47% | +1.65% |
| PLAY/USDT:USDT | below_1h_threshold | +1.44% | +1.61% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +1.39% | +1.57% |
| BTW/USDT:USDT | below_1h_threshold | +1.24% | +1.42% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
