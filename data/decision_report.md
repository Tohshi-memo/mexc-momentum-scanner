# Decision Report

- generated_at: 2026-06-17T04:06:44.226387+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6902**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6902, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/17 | 23.5% | -1.66% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| ASK_LONG | 20/20 | 100.0% | +2.24% | **+2.24%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +1.30% | **+0.52%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$193.93** / 初期 $100.00 (+93.93%)
- 確定: 1775件 (Win 476 / Loss 555 / Flat 744) / skip 1688件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $193.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定: 175件 (Win 36 / Loss 33 / Flat 106) / skip 138件
- 成長率目線: 平均log -0.000029 / 幾何平均 -0.003% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0787 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $99.49

## 5. Latest Market Context

- 更新: 2026-06-17T04:06:39.089176+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=65836.8
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +35.33% | $9,375,545.15 |
| ESPORTS/USDT:USDT | +24.62% | $3,756,560.28 |
| SPX/USDT:USDT | +22.87% | $6,825,800.65 |
| UNI/USDT:USDT | +17.37% | $42,986,836.47 |
| SQD/USDT:USDT | +16.92% | $1,414,693.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.81% | +4.77% |
| LAB/USDT:USDT | below_1h_threshold | +2.12% | +2.09% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.89% | +1.86% |
| XPL/USDT:USDT | below_1h_threshold | +1.76% | +1.73% |
| WLD/USDT:USDT | below_1h_threshold | +1.35% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
