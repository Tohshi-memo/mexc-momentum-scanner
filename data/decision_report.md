# Decision Report

- generated_at: 2026-06-14T03:15:25.623625+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6629**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=6629, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.98% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.22% | **+0.11%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.26% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.17** / 初期 $100.00 (+68.17%)
- 確定: 1502件 (Win 404 / Loss 481 / Flat 617) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.79% 残高後 $168.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 40件 (Win 13 / Loss 11 / Flat 16) / skip 0件
- 成長率目線: 平均log -0.000289 / 幾何平均 -0.029% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0200 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-14T03:15:19.798166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64456.2
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +44.91% | $3,801,858.14 |
| H/USDT:USDT | +32.90% | $19,870,591.31 |
| BTW/USDT:USDT | +21.02% | $2,035,098.84 |
| BRETT/USDT:USDT | +10.81% | $1,543,806.38 |
| JASMY/USDT:USDT | +8.54% | $3,316,023.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +0.99% | +0.98% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.99% | +0.98% |
| SIREN/USDT:USDT | below_1h_threshold | +0.76% | +0.76% |
| DASH/USDT:USDT | below_1h_threshold | +0.58% | +0.58% |
| CHZ/USDT:USDT | below_1h_threshold | +0.50% | +0.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
