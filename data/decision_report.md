# Decision Report

- generated_at: 2026-07-27T21:41:26.814828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9653**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9653, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.83% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.30% | **+0.77%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.13% | **+0.74%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.56% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$105.86** / 初期 $100.00 (+5.86%)
- 確定トレード: 147件 (TP 50 / SL 92 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.86
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3435件 (Win 1088 / Loss 1118 / Flat 1229) / skip 2779件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1840件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0138 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.61** / 初期 $100.00 (+8.61%)
- 確定: 673件 (Win 220 / Loss 255 / Flat 198) / pending 3件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.61

## 6. Latest Market Context

- 更新: 2026-07-27T21:41:17.162781+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64797.9
- Funnel: target 902 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +39.89% | $3,674,132.72 |
| JIMOTHY/USDT:USDT | +20.19% | $1,871,773.17 |
| SOONNETWORK/USDT:USDT | +12.91% | $1,193,349.31 |
| RIF/USDT:USDT | +9.58% | $6,966,592.21 |
| AKE/USDT:USDT | +7.05% | $43,956,873.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.42% | +4.64% |
| CAP/USDT:USDT | below_1h_threshold | +2.65% | +2.87% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.64% | +2.86% |
| PYTH/USDT:USDT | below_1h_threshold | +1.99% | +2.21% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.89% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
