# Decision Report

- generated_at: 2026-06-14T08:04:36.679914+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6652**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6652, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.13% | **+0.34%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.54** / 初期 $100.00 (+69.54%)
- 確定: 1525件 (Win 407 / Loss 486 / Flat 632) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $169.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.86** / 初期 $100.00 (-1.14%)
- 確定: 53件 (Win 17 / Loss 12 / Flat 24) / skip 10件
- 成長率目線: 平均log -0.000216 / 幾何平均 -0.022% per trade / maxDD +2.00%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.86

## 5. Latest Market Context

- 更新: 2026-06-14T08:04:31.168301+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64361.6
- Funnel: target 770 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +95.90% | $37,256,405.71 |
| TRADOOR/USDT:USDT | +38.50% | $6,760,298.90 |
| VELVET/USDT:USDT | +27.73% | $58,344,279.77 |
| MEGA/USDT:USDT | +18.15% | $4,491,071.91 |
| BTW/USDT:USDT | +13.49% | $3,014,156.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.07% | +4.12% |
| H/USDT:USDT | below_1h_threshold | +2.72% | +2.76% |
| BTW/USDT:USDT | below_1h_threshold | +1.65% | +1.69% |
| AIOT/USDT:USDT | below_1h_threshold | +0.69% | +0.73% |
| LAB/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
