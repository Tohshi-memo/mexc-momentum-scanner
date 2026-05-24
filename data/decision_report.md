# Decision Report

- generated_at: 2026-05-24T06:59:12.088112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4812**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4812, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.74% | **-0.26%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.48% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.56% | **+1.09%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.62% | **+0.89%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.06** / 初期 $100.00 (+21.06%)
- 確定: 618件 (Win 151 / Loss 196 / Flat 271) / skip 755件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $121.06

## 4. Latest Market Context

- 更新: 2026-05-24T06:59:09.644631+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=76957.7
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +35.50% | $1,187,137.53 |
| BLUAI/USDT:USDT | +15.62% | $1,782,052.27 |
| GRASS/USDT:USDT | +13.13% | $8,909,902.02 |
| SUPER/USDT:USDT | +12.80% | $1,725,254.62 |
| NIL/USDT:USDT | +12.68% | $2,492,421.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.03% | +2.80% |
| ARKM/USDT:USDT | below_1h_threshold | +3.00% | +2.77% |
| ONDO/USDT:USDT | below_1h_threshold | +2.83% | +2.60% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.32% | +2.09% |
| ME/USDT:USDT | below_1h_threshold | +2.19% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
