# Decision Report

- generated_at: 2026-08-13T05:21:27.379232+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11422**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11422, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.93% | **+1.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +7.96% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.99% | **+0.65%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.98% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.93% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.75% | **+1.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.55% | **+1.47%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.67% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.05** / 初期 $100.00 (+503.05%)
- 確定: 3950件 (Win 1232 / Loss 1292 / Flat 1426) / skip 4033件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.98** / 初期 $100.00 (+47.98%)
- 確定: 1610件 (Win 455 / Loss 379 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.89** / 初期 $100.00 (+14.89%)
- 確定: 1430件 (Win 418 / Loss 539 / Flat 473) / pending 5件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.89

## 6. Latest Market Context

- 更新: 2026-08-13T05:21:18.657746+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=63893.7
- Funnel: target 972 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +21.52% | $8,773,979.16 |
| CASHCAT/USDT:USDT | +10.94% | $1,023,159.54 |
| COOKIE/USDT:USDT | +8.91% | $1,036,505.99 |
| DELLSTOCK/USDT:USDT | +8.90% | $1,933,549.77 |
| BTW/USDT:USDT | +8.87% | $26,465,161.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.01% | +2.66% |
| BTW/USDT:USDT | below_1h_threshold | +1.77% | +1.43% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +0.94% |
| COTI/USDT:USDT | below_1h_threshold | +1.09% | +0.74% |
| RE/USDT:USDT | below_1h_threshold | +1.05% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
