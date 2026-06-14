# Decision Report

- generated_at: 2026-06-14T03:48:30.558967+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6633**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6633, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.54% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.85** / 初期 $100.00 (+69.85%)
- 確定: 1506件 (Win 405 / Loss 481 / Flat 620) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $169.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.99** / 初期 $100.00 (-1.01%)
- 確定: 44件 (Win 15 / Loss 11 / Flat 18) / skip 0件
- 成長率目線: 平均log -0.000231 / 幾何平均 -0.023% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.99

## 5. Latest Market Context

- 更新: 2026-06-14T03:48:25.789257+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64459.7
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 66.9 >= 65=1, 4h RSI 88.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +48.14% | $21,572,846.56 |
| TRADOOR/USDT:USDT | +43.90% | $4,078,579.07 |
| BTW/USDT:USDT | +26.71% | $2,371,544.61 |
| BRETT/USDT:USDT | +11.12% | $1,569,953.25 |
| MEGA/USDT:USDT | +10.41% | $4,040,425.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.81% | +4.79% |
| NOT/USDT:USDT | below_1h_threshold | +2.29% | +2.28% |
| JCT/USDT:USDT | below_1h_threshold | +1.91% | +1.90% |
| FET/USDT:USDT | below_1h_threshold | +1.10% | +1.08% |
| ALGO/USDT:USDT | below_1h_threshold | +0.99% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
