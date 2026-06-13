# Decision Report

- generated_at: 2026-06-13T16:07:29.949121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6589**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6589, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.08% | **+0.07%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.63% | **+1.45%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.04% | **+1.43%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.68% | **+1.34%** |
| ASK_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.52** / 初期 $100.00 (+66.52%)
- 確定: 1462件 (Win 392 / Loss 464 / Flat 606) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $166.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.07** / 初期 $100.00 (+0.07%)
- 確定: 2件 (Win 1 / Loss 0 / Flat 1) / skip 0件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +0.00%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $100.07

## 5. Latest Market Context

- 更新: 2026-06-13T16:07:25.139263+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=63992.6
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SQD/USDT:USDT | +5.36% | $1,817,823.98 |
| COAI/USDT:USDT | +5.07% | $15,922,096.49 |
| PIPPIN/USDT:USDT | +2.06% | $2,091,216.33 |
| FOLKS/USDT:USDT | +2.00% | $1,427,000.01 |
| AIN/USDT:USDT | +1.85% | $1,077,181.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +4.42% | +4.84% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.95% | +2.37% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.94% | +2.37% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.90% | +2.32% |
| AIN/USDT:USDT | below_1h_threshold | +1.85% | +2.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
