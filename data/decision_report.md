# Decision Report

- generated_at: 2026-06-05T23:32:10.066379+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5767**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5767, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.61% | **+0.65%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.56% | **+2.05%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.63% | **+1.58%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1316件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T23:32:07.594914+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.37% price=60710.4
- Funnel: target 771 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +25.21% | $1,536,156.74 |
| ZEST/USDT:USDT | +22.76% | $2,390,271.80 |
| ALLO/USDT:USDT | +19.37% | $7,196,023.89 |
| HOME/USDT:USDT | +17.84% | $6,805,008.02 |
| BTW/USDT:USDT | +16.70% | $35,065,830.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.71% | +6.09% |
| GUA/USDT:USDT | below_1h_threshold | +4.65% | +6.02% |
| OPN/USDT:USDT | below_1h_threshold | +4.59% | +5.97% |
| BTW/USDT:USDT | below_1h_threshold | +1.87% | +3.25% |
| ZEC/USDT:USDT | below_1h_threshold | +1.82% | +3.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
