# Decision Report

- generated_at: 2026-05-07T17:17:37.001125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3670**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3670, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 13/20 | 65.0% | +2.58% | **+1.68%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.15% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.74% | **+1.92%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.21% | **+1.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.88% | **+1.30%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.07** / 初期 $100.00 (+10.07%)
- 確定: 164件 (Win 46 / Loss 57 / Flat 61) / skip 67件
- 成長率目線: 平均log +0.000585 / 幾何平均 +0.059% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $110.07

## 4. Latest Market Context

- 更新: 2026-05-07T17:17:34.191433+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79773.3
- Funnel: target 771 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +25.53% | $5,142,723.59 |
| JTO/USDT:USDT | +20.57% | $9,673,190.24 |
| B/USDT:USDT | +13.65% | $4,366,803.15 |
| BILL/USDT:USDT | +6.78% | $12,273,349.07 |
| HIGH/USDT:USDT | +6.72% | $1,446,562.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.35% | +4.33% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.50% | +3.49% |
| B/USDT:USDT | below_1h_threshold | +2.54% | +2.53% |
| LUNC/USDT:USDT | below_1h_threshold | +2.53% | +2.52% |
| DOGS/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
