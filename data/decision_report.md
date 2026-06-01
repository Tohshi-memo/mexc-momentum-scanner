# Decision Report

- generated_at: 2026-06-01T01:20:03.493326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5253**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5253, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.19% | **+0.48%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.81% | **+1.45%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.26% | **+1.14%** |
| LIMIT_BB3S_LONG | 8/12 | 66.7% | +1.44% | **+0.96%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.55% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.33** / 初期 $100.00 (+33.33%)
- 確定: 887件 (Win 206 / Loss 264 / Flat 417) / skip 927件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IBMSTOCK/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account -0.17% 残高後 $133.33

## 4. Latest Market Context

- 更新: 2026-06-01T01:20:00.385808+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=73570.1
- Funnel: target 775 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +165.76% | $22,868,248.55 |
| H/USDT:USDT | +53.14% | $16,445,572.19 |
| STG/USDT:USDT | +28.47% | $21,883,297.36 |
| HOME/USDT:USDT | +21.95% | $3,537,743.80 |
| CTR/USDT:USDT | +21.43% | $1,407,717.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.72% | +5.10% |
| CTR/USDT:USDT | below_1h_threshold | +3.70% | +4.09% |
| APE/USDT:USDT | below_1h_threshold | +2.51% | +2.89% |
| NEX/USDT:USDT | below_1h_threshold | +0.85% | +1.24% |
| STG/USDT:USDT | below_1h_threshold | +0.71% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
