# Decision Report

- generated_at: 2026-10-27T16:41:38.763579+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17628**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17628, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +5.20% | **+2.08%** |
| LIMIT_9PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +3.15% | **+1.58%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.70% | **+2.96%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.70% | **+2.59%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.82% | **+2.10%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.33% | **+1.95%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.25% | **+1.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,565.50** / 初期 $100.00 (+1465.50%)
- 確定: 6737件 (Win 1963 / Loss 2158 / Flat 2616) / skip 7452件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,565.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$346.41** / 初期 $100.00 (+246.41%)
- 確定: 4157件 (Win 1138 / Loss 963 / Flat 2056) / skip 6882件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1086 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $346.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5789件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000423 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T16:41:21.414147+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80647.1
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +41.48% | $11,311,999.21 |
| AKE/USDT:USDT | +20.89% | $4,837,321.97 |
| CBRSSTOCK/USDT:USDT | +5.42% | $1,792,600.98 |
| LAB/USDT:USDT | +3.24% | $1,064,312.45 |
| ZEC/USDT:USDT | +1.64% | $1,483,061,779.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.32% | +3.17% |
| ZEC/USDT:USDT | below_1h_threshold | +1.71% | +1.56% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.55% | +1.40% |
| AIN/USDT:USDT | below_1h_threshold | +1.42% | +1.28% |
| DASH/USDT:USDT | below_1h_threshold | +1.33% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
