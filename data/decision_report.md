# Decision Report

- generated_at: 2026-08-03T11:16:14.785820+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10208**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10208, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.33% | **+0.44%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.06% | **+0.61%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.65% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3677件 (Win 1166 / Loss 1205 / Flat 1306) / skip 3092件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2336件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.40** / 初期 $100.00 (+13.40%)
- 確定: 994件 (Win 316 / Loss 389 / Flat 289) / pending 5件 / skip 682件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $113.40

## 6. Latest Market Context

- 更新: 2026-08-03T11:16:08.906086+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62631.6
- Funnel: target 929 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +128.38% | $1,668,946.81 |
| BICO/USDT:USDT | +43.15% | $9,926,428.91 |
| 1000RATS/USDT:USDT | +42.04% | $36,060,315.84 |
| ALLO/USDT:USDT | +21.20% | $5,559,574.56 |
| BLESS/USDT:USDT | +19.75% | $84,194,172.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.58% | +4.70% |
| SOXS/USDT:USDT | below_1h_threshold | +1.99% | +2.11% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.76% | +1.88% |
| ALLO/USDT:USDT | below_1h_threshold | +1.32% | +1.44% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.46% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
