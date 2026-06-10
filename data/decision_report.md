# Decision Report

- generated_at: 2026-06-10T07:24:33.099638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6196**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6196, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.50% | **+0.07%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| ASK | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.45% | **+0.65%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.04** / 初期 $100.00 (+49.04%)
- 確定: 1212件 (Win 300 / Loss 376 / Flat 536) / skip 1545件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $149.04

## 4. Latest Market Context

- 更新: 2026-06-10T07:24:29.119055+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=61632.6
- Funnel: target 781 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +41.65% | $6,899,742.25 |
| BTW/USDT:USDT | +34.68% | $29,383,743.79 |
| UB/USDT:USDT | +16.01% | $1,943,715.61 |
| ESPORTS/USDT:USDT | +12.80% | $21,763,163.80 |
| UAI/USDT:USDT | +12.13% | $1,495,293.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +4.90% | +4.58% |
| WLFI/USDT:USDT | below_1h_threshold | +2.94% | +2.62% |
| DYDX/USDT:USDT | below_1h_threshold | +2.65% | +2.33% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.08% | +1.76% |
| FET/USDT:USDT | below_1h_threshold | +1.97% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
