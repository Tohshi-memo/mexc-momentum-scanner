# Decision Report

- generated_at: 2026-06-14T05:55:10.743457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6645**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6645, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.50% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.54** / 初期 $100.00 (+69.54%)
- 確定: 1518件 (Win 407 / Loss 486 / Flat 625) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +1.00% 残高後 $169.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.86** / 初期 $100.00 (-1.14%)
- 確定: 50件 (Win 17 / Loss 12 / Flat 21) / skip 6件
- 成長率目線: 平均log -0.000229 / 幾何平均 -0.023% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.86

## 5. Latest Market Context

- 更新: 2026-06-14T05:55:04.401635+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64339.2
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1, 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +79.49% | $28,307,207.75 |
| TRADOOR/USDT:USDT | +45.70% | $5,809,010.11 |
| BTW/USDT:USDT | +24.23% | $2,699,708.99 |
| MEGA/USDT:USDT | +14.00% | $4,253,386.06 |
| VELVET/USDT:USDT | +13.61% | $57,336,838.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.48% | +4.42% |
| TRADOOR/USDT:USDT | below_1h_threshold | +4.13% | +4.07% |
| JASMY/USDT:USDT | below_1h_threshold | +3.25% | +3.19% |
| HOME/USDT:USDT | below_1h_threshold | +2.52% | +2.46% |
| PLAY/USDT:USDT | below_1h_threshold | +2.13% | +2.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
