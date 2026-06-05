# Decision Report

- generated_at: 2026-06-05T02:54:59.718544+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5695, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.77% | **-0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.87% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.31% | **+1.38%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.90% | **+1.04%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.05% | **+1.02%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1009件 (Win 239 / Loss 312 / Flat 458) / skip 1247件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T02:54:56.836792+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.07% price=62666.9
- Funnel: target 772 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +84.88% | $13,519,908.87 |
| HOME/USDT:USDT | +18.14% | $7,806,507.78 |
| OPN/USDT:USDT | +13.74% | $36,467,496.61 |
| ZEST/USDT:USDT | +12.41% | $5,444,899.72 |
| HEI/USDT:USDT | +11.48% | $5,409,809.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +2.39% |
| ALLO/USDT:USDT | below_1h_threshold | +1.10% | +2.17% |
| HEI/USDT:USDT | below_1h_threshold | +1.10% | +2.17% |
| ASTER/USDT:USDT | below_1h_threshold | +0.66% | +1.74% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.39% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
