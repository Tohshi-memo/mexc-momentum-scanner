# Decision Report

- generated_at: 2026-05-07T06:32:54.651450+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3579**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3579, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +2.00% | **+0.55%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.78% | **+0.50%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.20% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.82% | **+0.74%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.69** / 初期 $100.00 (+6.69%)
- 確定: 73件 (Win 27 / Loss 29 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.000887 / 幾何平均 +0.089% per trade / maxDD +2.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $106.69

## 4. Latest Market Context

- 更新: 2026-05-07T06:32:51.152323+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=81097.9
- Funnel: target 770 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1, 4h RSI 81.6 >= 65=1, 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +276.87% | $1,791,426.77 |
| B3/USDT:USDT | +91.13% | $9,611,888.03 |
| DOGS/USDT:USDT | +70.27% | $12,500,799.33 |
| PENGUIN/USDT:USDT | +57.55% | $1,418,805.39 |
| FHE/USDT:USDT | +32.97% | $17,001,181.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.62% | +4.56% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.67% | +2.60% |
| VVV/USDT:USDT | below_1h_threshold | +1.74% | +1.68% |
| H/USDT:USDT | below_1h_threshold | +1.29% | +1.22% |
| SILVER/USDT:USDT | below_1h_threshold | +1.12% | +1.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
