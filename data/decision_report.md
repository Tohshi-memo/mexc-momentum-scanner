# Decision Report

- generated_at: 2026-05-22T10:48:58.074486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4687**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4687, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.46% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.75% | **+1.97%** |
| ASK_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.84** / 初期 $100.00 (+21.84%)
- 確定: 557件 (Win 141 / Loss 185 / Flat 231) / skip 691件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.84

## 4. Latest Market Context

- 更新: 2026-05-22T10:48:53.452536+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77294.6
- Funnel: target 768 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +44.46% | $3,561,916.77 |
| ALT/USDT:USDT | +33.80% | $1,814,897.82 |
| GENIUS/USDT:USDT | +32.54% | $1,530,665.42 |
| EDEN/USDT:USDT | +29.50% | $21,549,608.31 |
| BEAT/USDT:USDT | +28.89% | $12,711,318.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.59% | +3.55% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +3.45% | +3.42% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.28% | +3.24% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.88% | +2.85% |
| PLAY/USDT:USDT | below_1h_threshold | +2.80% | +2.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
