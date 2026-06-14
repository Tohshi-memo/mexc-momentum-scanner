# Decision Report

- generated_at: 2026-06-14T04:23:11.936912+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6635**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6635, expectancy=-0.05%
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
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.54% | **+0.23%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.54% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.00** / 初期 $100.00 (+69.00%)
- 確定: 1508件 (Win 405 / Loss 482 / Flat 621) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $169.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.64** / 初期 $100.00 (-1.36%)
- 確定: 45件 (Win 15 / Loss 12 / Flat 18) / skip 1件
- 成長率目線: 平均log -0.000304 / 幾何平均 -0.030% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $98.64

## 5. Latest Market Context

- 更新: 2026-06-14T04:14:23.998414+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64465.4
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +59.12% | $22,998,158.66 |
| TRADOOR/USDT:USDT | +44.38% | $4,254,659.67 |
| BTW/USDT:USDT | +23.21% | $2,464,122.62 |
| BRETT/USDT:USDT | +14.66% | $1,518,025.67 |
| JCT/USDT:USDT | +10.62% | $10,662,881.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +2.63% | +2.71% |
| SIREN/USDT:USDT | below_1h_threshold | +2.61% | +2.69% |
| JCT/USDT:USDT | below_1h_threshold | +1.67% | +1.74% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.45% | +1.53% |
| SQD/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
