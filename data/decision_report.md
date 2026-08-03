# Decision Report

- generated_at: 2026-08-03T08:02:06.819357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10200**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10200, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.17% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.31% | **+0.23%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.42% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.91% | **+0.76%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.26% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3677件 (Win 1166 / Loss 1205 / Flat 1306) / skip 3084件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2329件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0032 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.08** / 初期 $100.00 (+13.08%)
- 確定: 986件 (Win 313 / Loss 386 / Flat 287) / pending 1件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000261 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ICNT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $113.08

## 6. Latest Market Context

- 更新: 2026-08-03T08:02:00.912440+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62588.4
- Funnel: target 924 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +80.09% | $1,194,927.36 |
| 1000RATS/USDT:USDT | +45.98% | $37,733,747.90 |
| BICO/USDT:USDT | +20.95% | $7,408,062.53 |
| GRVT/USDT:USDT | +16.14% | $2,355,716.34 |
| TAKE/USDT:USDT | +15.39% | $1,405,695.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.28% | +3.28% |
| GRVT/USDT:USDT | below_1h_threshold | +1.32% | +1.33% |
| SOXS/USDT:USDT | below_1h_threshold | +0.70% | +0.71% |
| FHE/USDT:USDT | below_1h_threshold | +0.64% | +0.65% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
