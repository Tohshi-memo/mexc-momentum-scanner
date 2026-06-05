# Decision Report

- generated_at: 2026-06-05T10:34:26.436537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5711, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.84% | **+0.64%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.13%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.43%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.32% | **+0.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.21% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1262件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T10:34:23.028636+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=62562.1
- Funnel: target 773 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +80.48% | $23,231,495.19 |
| BABY/USDT:USDT | +64.24% | $4,664,819.75 |
| CLO/USDT:USDT | +19.04% | $1,102,273.54 |
| OPN/USDT:USDT | +16.13% | $40,607,606.06 |
| AAOISTOCK/USDT:USDT | +11.39% | $2,055,769.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APPSTOCK/USDT:USDT | below_1h_threshold | +3.08% | +3.50% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +0.65% | +1.08% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.58% | +1.01% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.96% |
| LMTSTOCK/USDT:USDT | below_1h_threshold | +0.44% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
