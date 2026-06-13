# Decision Report

- generated_at: 2026-06-13T21:58:58.844599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6613**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6613, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.00% | **+1.50%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.47% | **+1.48%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.32** / 初期 $100.00 (+69.32%)
- 確定: 1486件 (Win 401 / Loss 474 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.71% 残高後 $169.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 24件 (Win 8 / Loss 10 / Flat 6) / skip 0件
- 成長率目線: 平均log -0.000482 / 幾何平均 -0.048% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0177 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-13T21:58:53.976017+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=64465.9
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +20.97% | $10,535,287.56 |
| MEGA/USDT:USDT | +13.26% | $2,327,391.27 |
| BTW/USDT:USDT | +10.75% | $1,866,557.75 |
| COAI/USDT:USDT | +6.07% | $32,538,461.62 |
| BILL/USDT:USDT | +5.73% | $2,168,328.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_relative_strength | +5.27% | +4.94% |
| COAI/USDT:USDT | below_1h_threshold | +4.27% | +3.94% |
| ZEC/USDT:USDT | below_1h_threshold | +3.18% | +2.84% |
| BILL/USDT:USDT | below_1h_threshold | +3.04% | +2.71% |
| JASMY/USDT:USDT | below_1h_threshold | +2.37% | +2.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
