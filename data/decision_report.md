# Decision Report

- generated_at: 2026-06-13T22:05:15.412926+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6614**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6614, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.56** / 初期 $100.00 (+68.56%)
- 確定: 1487件 (Win 401 / Loss 475 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.45% 残高後 $168.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 25件 (Win 8 / Loss 10 / Flat 7) / skip 0件
- 成長率目線: 平均log -0.000462 / 幾何平均 -0.046% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0187 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-13T22:05:10.598573+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64419.7
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +22.05% | $10,642,449.44 |
| MEGA/USDT:USDT | +12.90% | $2,312,963.27 |
| BTW/USDT:USDT | +8.41% | $1,850,831.18 |
| BILL/USDT:USDT | +6.08% | $2,004,438.32 |
| JASMY/USDT:USDT | +6.07% | $1,420,213.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +1.42% | +1.44% |
| H/USDT:USDT | below_1h_threshold | +1.00% | +1.03% |
| JUP/USDT:USDT | below_1h_threshold | +0.80% | +0.83% |
| SQD/USDT:USDT | below_1h_threshold | +0.55% | +0.58% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.40% | +0.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
