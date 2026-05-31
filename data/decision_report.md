# Decision Report

- generated_at: 2026-05-31T22:25:00.713428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5233**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5233, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.38% | **+0.71%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_BB3S | 8/16 | 50.0% | +0.62% | **+0.31%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.28% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.78% | **+1.81%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.11% | **+1.71%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.54% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.13** / 初期 $100.00 (+34.13%)
- 確定: 868件 (Win 203 / Loss 258 / Flat 407) / skip 926件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $134.13

## 4. Latest Market Context

- 更新: 2026-05-31T22:24:57.921072+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=73845.9
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +79.35% | $14,976,931.45 |
| STG/USDT:USDT | +39.28% | $19,220,428.97 |
| HOME/USDT:USDT | +13.11% | $3,044,287.09 |
| BIANRENSHENG/USDT:USDT | +12.15% | $3,132,025.31 |
| ZORA/USDT:USDT | +11.59% | $1,595,121.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.87% | +2.89% |
| LIT/USDT:USDT | below_1h_threshold | +1.99% | +2.01% |
| BSB/USDT:USDT | below_1h_threshold | +1.80% | +1.82% |
| XLM/USDT:USDT | below_1h_threshold | +1.78% | +1.80% |
| NEX/USDT:USDT | below_1h_threshold | +1.31% | +1.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
