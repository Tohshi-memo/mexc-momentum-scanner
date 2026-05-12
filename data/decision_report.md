# Decision Report

- generated_at: 2026-05-12T18:28:15.767875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4153**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4153, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.37% | **-0.09%** |
| ASK | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.52% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.59** / 初期 $100.00 (+20.59%)
- 確定: 289件 (Win 83 / Loss 99 / Flat 107) / skip 425件
- 成長率目線: 平均log +0.000648 / 幾何平均 +0.065% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $120.59

## 4. Latest Market Context

- 更新: 2026-05-12T18:28:12.525539+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80463.8
- Funnel: target 759 → liquid 196 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +17.74% | $4,162,220.09 |
| IRYS/USDT:USDT | +7.95% | $2,097,116.26 |
| DYM/USDT:USDT | +6.86% | $1,623,962.30 |
| ATOM/USDT:USDT | +5.22% | $26,846,039.34 |
| LAB/USDT:USDT | +5.02% | $170,874,823.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYM/USDT:USDT | below_1h_threshold | +2.99% | +3.03% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.36% | +2.39% |
| ATOM/USDT:USDT | below_1h_threshold | +2.22% | +2.26% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.00% | +2.04% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.99% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
