# Decision Report

- generated_at: 2026-08-03T10:21:08.121503+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10206**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10206, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.95% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.35% | **+0.26%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.89% | **+0.63%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.24% | **+0.56%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.79% | **+0.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.34% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3677件 (Win 1166 / Loss 1205 / Flat 1306) / skip 3090件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2335件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0034 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.10** / 初期 $100.00 (+13.10%)
- 確定: 992件 (Win 315 / Loss 389 / Flat 288) / pending 2件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $113.10

## 6. Latest Market Context

- 更新: 2026-08-03T10:21:03.039915+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62757.1
- Funnel: target 929 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +99.33% | $1,385,942.88 |
| 1000RATS/USDT:USDT | +54.17% | $37,077,306.48 |
| BICO/USDT:USDT | +29.20% | $8,772,571.60 |
| BLESS/USDT:USDT | +19.77% | $84,694,650.15 |
| BTW/USDT:USDT | +16.75% | $6,169,024.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.55% | +2.62% |
| ALLO/USDT:USDT | below_1h_threshold | +2.47% | +2.54% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.35% | +2.43% |
| NIL/USDT:USDT | below_1h_threshold | +1.98% | +2.05% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.68% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
