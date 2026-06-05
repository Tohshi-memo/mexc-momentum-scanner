# Decision Report

- generated_at: 2026-06-05T20:00:15.006654+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5757**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5757, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.29% | **+1.50%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.74% | **+0.70%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1011件 (Win 239 / Loss 313 / Flat 459) / skip 1307件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T20:00:05.430546+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.57% price=60292.8
- Funnel: target 772 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=3, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +27.57% | $34,246,105.87 |
| GUA/USDT:USDT | +15.56% | $1,878,996.61 |
| HOME/USDT:USDT | +15.12% | $7,348,762.83 |
| ALLO/USDT:USDT | +13.87% | $6,491,769.92 |
| OPN/USDT:USDT | +13.81% | $36,097,269.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +6.03% | +4.47% |
| PORTAL/USDT:USDT | below_relative_strength | +5.53% | +3.96% |
| BTW/USDT:USDT | below_relative_strength | +5.38% | +3.81% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +4.75% | +3.18% |
| VVV/USDT:USDT | below_1h_threshold | +4.48% | +2.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
