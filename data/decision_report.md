# Decision Report

- generated_at: 2026-09-21T12:21:24.165679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15257, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/15 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.53% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.05% | **+1.68%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +4.18% | **+1.04%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.62% | **+0.89%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.46% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,170.79** / 初期 $100.00 (+1070.79%)
- 確定: 5748件 (Win 1712 / Loss 1849 / Flat 2187) / skip 6070件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,170.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3314件 (Win 915 / Loss 765 / Flat 1634) / skip 5354件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0007 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.26** / 初期 $100.00 (+22.26%)
- 確定: 3034件 (Win 892 / Loss 1188 / Flat 954) / pending 3件 / skip 3691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000101 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.26

## 6. Latest Market Context

- 更新: 2026-09-21T12:21:13.337612+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=85206.6
- Funnel: target 1053 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +77.59% | $7,475,791.71 |
| PHA/USDT:USDT | +64.32% | $5,349,668.39 |
| PTB/USDT:USDT | +34.40% | $1,173,751.30 |
| NIL/USDT:USDT | +29.85% | $7,721,054.11 |
| UAI/USDT:USDT | +29.20% | $1,906,517.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.23% | +2.81% |
| ZETA/USDT:USDT | below_1h_threshold | +3.20% | +2.78% |
| WIF/USDT:USDT | below_1h_threshold | +3.20% | +2.78% |
| PHA/USDT:USDT | below_1h_threshold | +2.96% | +2.54% |
| NIL/USDT:USDT | below_1h_threshold | +2.56% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
