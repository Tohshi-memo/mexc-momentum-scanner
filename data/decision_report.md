# Decision Report

- generated_at: 2026-05-07T17:07:41.549611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3669**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3669, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +2.71% | **+1.63%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.21% | **+1.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.88% | **+1.30%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.07** / 初期 $100.00 (+10.07%)
- 確定: 163件 (Win 46 / Loss 57 / Flat 60) / skip 67件
- 成長率目線: 平均log +0.000589 / 幾何平均 +0.059% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $110.07

## 4. Latest Market Context

- 更新: 2026-05-07T17:07:38.459876+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=79894.6
- Funnel: target 771 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JTO/USDT:USDT | +17.68% | $8,138,962.15 |
| B/USDT:USDT | +13.48% | $4,208,664.52 |
| SATO/USDT:USDT | +11.32% | $5,053,592.79 |
| BILL/USDT:USDT | +7.57% | $12,123,267.09 |
| HIGH/USDT:USDT | +7.39% | $1,422,013.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +2.78% | +2.62% |
| B/USDT:USDT | below_1h_threshold | +2.38% | +2.22% |
| DYDX/USDT:USDT | below_1h_threshold | +1.78% | +1.62% |
| JTO/USDT:USDT | below_1h_threshold | +1.66% | +1.50% |
| BILL/USDT:USDT | below_1h_threshold | +1.58% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
