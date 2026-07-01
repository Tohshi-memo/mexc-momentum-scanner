# Decision Report

- generated_at: 2026-07-01T04:58:32.165833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7951**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7951, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.09% | **-0.09%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.71% | **+0.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.49% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2156件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.84** / 初期 $100.00 (+6.84%)
- 確定: 493件 (Win 127 / Loss 121 / Flat 245) / skip 869件
- 成長率目線: 平均log +0.000134 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0334 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.84

## 5. Latest Market Context

- 更新: 2026-07-01T04:58:23.618356+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=59303.6
- Funnel: target 823 → liquid 152 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1, 4h RSI 67.0 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYDX/USDT:USDT | +34.97% | $6,851,461.24 |
| BEAT/USDT:USDT | +29.70% | $25,603,785.80 |
| TAIKO/USDT:USDT | +24.00% | $1,616,574.77 |
| BTW/USDT:USDT | +18.97% | $11,568,733.79 |
| TRIA/USDT:USDT | +16.34% | $1,048,915.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPX/USDT:USDT | below_1h_threshold | +3.01% | +2.78% |
| ZBT/USDT:USDT | below_1h_threshold | +2.76% | +2.54% |
| JTO/USDT:USDT | below_1h_threshold | +2.68% | +2.46% |
| TRIA/USDT:USDT | below_1h_threshold | +1.91% | +1.68% |
| XPL/USDT:USDT | below_1h_threshold | +1.73% | +1.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
