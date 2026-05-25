# Decision Report

- generated_at: 2026-05-25T04:44:07.562432+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4842**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4842, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.69% | **+0.31%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.20% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.16** / 初期 $100.00 (+24.16%)
- 確定: 648件 (Win 161 / Loss 206 / Flat 281) / skip 755件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.72% 残高後 $124.16

## 4. Latest Market Context

- 更新: 2026-05-25T04:44:05.470975+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77192.9
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +30.31% | $2,206,454.14 |
| SPORTFUN/USDT:USDT | +13.21% | $1,219,431.41 |
| H/USDT:USDT | +8.20% | $1,070,177.98 |
| SAGA/USDT:USDT | +5.77% | $1,269,750.87 |
| LUNC/USDT:USDT | +4.06% | $2,612,287.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHZ/USDT:USDT | below_1h_threshold | +2.19% | +1.93% |
| XAN/USDT:USDT | below_1h_threshold | +1.84% | +1.58% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.75% | +1.49% |
| SPX/USDT:USDT | below_1h_threshold | +1.53% | +1.27% |
| H/USDT:USDT | below_1h_threshold | +1.45% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
