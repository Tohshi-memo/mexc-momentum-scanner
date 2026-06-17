# Decision Report

- generated_at: 2026-06-17T08:17:11.105513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6915**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6915, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.03% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.96% | **+2.98%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.82** / 初期 $100.00 (+97.82%)
- 確定: 1788件 (Win 484 / Loss 559 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $197.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 188件 (Win 42 / Loss 37 / Flat 109) / skip 138件
- 成長率目線: 平均log +0.000048 / 幾何平均 +0.005% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0927 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $100.91

## 5. Latest Market Context

- 更新: 2026-06-17T08:17:06.280974+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=65296.4
- Funnel: target 784 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +38.84% | $4,612,426.56 |
| SQD/USDT:USDT | +26.78% | $2,285,384.45 |
| ROAM/USDT:USDT | +26.70% | $3,038,339.77 |
| UNI/USDT:USDT | +18.90% | $52,499,711.75 |
| SPX/USDT:USDT | +17.28% | $8,564,177.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.11% | +2.43% |
| LIT/USDT:USDT | below_1h_threshold | +1.88% | +2.20% |
| PLAY/USDT:USDT | below_1h_threshold | +1.70% | +2.01% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.06% | +1.38% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +1.06% | +1.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
