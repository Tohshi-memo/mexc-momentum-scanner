# Decision Report

- generated_at: 2026-06-13T16:25:45.504198+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6591**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6591, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.24% | **+0.05%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.07% | **+1.14%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.66% | **+0.75%** |
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$165.69** / 初期 $100.00 (+65.69%)
- 確定: 1464件 (Win 392 / Loss 465 / Flat 607) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $165.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.72** / 初期 $100.00 (-0.28%)
- 確定: 3件 (Win 1 / Loss 1 / Flat 1) / skip 0件
- 成長率目線: 平均log -0.000935 / 幾何平均 -0.093% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0175 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.72

## 5. Latest Market Context

- 更新: 2026-06-13T16:25:40.052817+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=63933.6
- Funnel: target 770 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SQD/USDT:USDT | +8.88% | $1,929,188.32 |
| JCT/USDT:USDT | +2.38% | $9,800,296.02 |
| SKYAI/USDT:USDT | +2.10% | $17,874,430.71 |
| AIN/USDT:USDT | +2.09% | $1,087,064.38 |
| ESPORTS/USDT:USDT | +1.38% | $66,491,901.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.38% | +2.90% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.10% | +2.62% |
| AIN/USDT:USDT | below_1h_threshold | +2.09% | +2.61% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.88% | +2.39% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.04% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
