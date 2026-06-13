# Decision Report

- generated_at: 2026-06-13T19:30:12.270653+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6607**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6607, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.58** / 初期 $100.00 (+67.58%)
- 確定: 1480件 (Win 398 / Loss 471 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $167.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.76** / 初期 $100.00 (-0.24%)
- 確定: 18件 (Win 6 / Loss 7 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.000136 / 幾何平均 -0.014% per trade / maxDD +1.05%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0569 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.76

## 5. Latest Market Context

- 更新: 2026-06-13T19:30:07.174238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64154.1
- Funnel: target 770 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COAI/USDT:USDT | +18.01% | $26,054,188.84 |
| RIF/USDT:USDT | +13.79% | $7,421,232.49 |
| AT/USDT:USDT | +13.48% | $1,041,581.82 |
| VELVET/USDT:USDT | +13.27% | $64,203,919.59 |
| NOT/USDT:USDT | +4.63% | $2,790,304.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +3.62% | +3.57% |
| AT/USDT:USDT | below_1h_threshold | +2.63% | +2.58% |
| RIF/USDT:USDT | below_1h_threshold | +2.24% | +2.19% |
| JCT/USDT:USDT | below_1h_threshold | +1.82% | +1.77% |
| AIOT/USDT:USDT | below_1h_threshold | +1.26% | +1.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
