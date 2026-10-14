# Decision Report

- generated_at: 2026-10-14T15:11:29.792739+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16681**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16681, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,278.87** / 初期 $100.00 (+1178.87%)
- 確定: 6297件 (Win 1845 / Loss 2018 / Flat 2434) / skip 6945件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1618_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1618_LONG` EXPIRED account +0.00% 残高後 $1,278.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.76** / 初期 $100.00 (+170.76%)
- 確定: 3654件 (Win 1015 / Loss 864 / Flat 1775) / skip 6438件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4841件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T15:11:17.932406+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81685.3
- Funnel: target 1085 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSPSTOCK/USDT:USDT | +36.81% | $1,658,509.32 |
| WAL/USDT:USDT | +31.54% | $5,427,461.68 |
| TRUTH/USDT:USDT | +27.93% | $4,084,890.51 |
| BTW/USDT:USDT | +25.55% | $56,970,110.74 |
| AVA/USDT:USDT | +23.21% | $1,242,115.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSPSTOCK/USDT:USDT | below_1h_threshold | +3.14% | +3.44% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.51% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +1.04% |
| BTW/USDT:USDT | below_1h_threshold | +0.64% | +0.94% |
| AKE/USDT:USDT | below_1h_threshold | +0.10% | +0.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
