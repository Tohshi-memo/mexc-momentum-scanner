# Decision Report

- generated_at: 2026-07-30T19:56:29.728226+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9921, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.92% | **-2.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.04% | **+0.01%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.51% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.26% | **+2.77%** |
| MARKET_LONG | 20/20 | 100.0% | +2.51% | **+2.51%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.82% | **+2.29%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.60% | **+1.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$502.14** / 初期 $100.00 (+402.14%)
- 確定: 3522件 (Win 1115 / Loss 1147 / Flat 1260) / skip 2960件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $502.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2089件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1132 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定: 803件 (Win 262 / Loss 318 / Flat 223) / pending 2件 / skip 595件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AGT/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $110.80

## 6. Latest Market Context

- 更新: 2026-07-30T19:56:19.582427+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64786.4
- Funnel: target 920 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +20.91% | $4,180,733.80 |
| MMT/USDT:USDT | +18.47% | $6,089,039.92 |
| CAP/USDT:USDT | +17.06% | $4,083,258.11 |
| ROBO/USDT:USDT | +16.43% | $2,680,071.93 |
| EVAA/USDT:USDT | +13.06% | $3,138,917.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.47% | +3.28% |
| EVAA/USDT:USDT | below_1h_threshold | +3.18% | +2.99% |
| ROBO/USDT:USDT | below_1h_threshold | +3.10% | +2.92% |
| MMT/USDT:USDT | below_1h_threshold | +2.92% | +2.74% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.71% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
