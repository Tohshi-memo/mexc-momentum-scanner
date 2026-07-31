# Decision Report

- generated_at: 2026-07-31T15:01:24.734295+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10014, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.62% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 3002件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2147件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0085 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.82** / 初期 $100.00 (+10.82%)
- 確定: 845件 (Win 272 / Loss 335 / Flat 238) / pending 6件 / skip 637件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.82

## 6. Latest Market Context

- 更新: 2026-07-31T15:01:16.088512+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62603.0
- Funnel: target 921 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +106.15% | $3,313,515.02 |
| KOMA/USDT:USDT | +86.42% | $14,541,416.73 |
| GIGGLE/USDT:USDT | +34.04% | $11,364,731.70 |
| AXTISTOCK/USDT:USDT | +30.33% | $10,076,830.72 |
| AMZU/USDT:USDT | +27.43% | $1,856,701.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GGLL/USDT:USDT | below_1h_threshold | +4.93% | +5.03% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +2.55% | +2.64% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.40% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.63% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.18% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
