# Decision Report

- generated_at: 2026-06-14T06:26:15.083938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6646**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6646, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.50% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.81%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.54** / 初期 $100.00 (+69.54%)
- 確定: 1519件 (Win 407 / Loss 486 / Flat 626) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $169.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.86** / 初期 $100.00 (-1.14%)
- 確定: 51件 (Win 17 / Loss 12 / Flat 22) / skip 6件
- 成長率目線: 平均log -0.000224 / 幾何平均 -0.022% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0337 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.86

## 5. Latest Market Context

- 更新: 2026-06-14T06:26:11.008483+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64323.8
- Funnel: target 770 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +86.82% | $30,093,126.06 |
| TRADOOR/USDT:USDT | +44.62% | $6,083,520.31 |
| BTW/USDT:USDT | +21.70% | $2,705,184.19 |
| VELVET/USDT:USDT | +17.44% | $57,524,548.82 |
| MEGA/USDT:USDT | +16.03% | $4,310,915.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +3.32% | +3.30% |
| WLD/USDT:USDT | below_1h_threshold | +2.27% | +2.25% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.19% | +2.17% |
| JASMY/USDT:USDT | below_1h_threshold | +1.22% | +1.20% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.16% | +1.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
