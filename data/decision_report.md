# Decision Report

- generated_at: 2026-07-20T08:36:28.042830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9098, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.74% | **-1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.55% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.56% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +7.79% | **+3.90%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.62% | **+1.97%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.77% | **+1.25%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.32% | **+1.05%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定トレード: 121件 (TP 43 / SL 73 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -3.98% 残高後 $108.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$397.88** / 初期 $100.00 (+297.88%)
- 確定: 3160件 (Win 987 / Loss 1003 / Flat 1170) / skip 2499件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $397.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.54** / 初期 $100.00 (+26.54%)
- 確定: 1059件 (Win 275 / Loss 218 / Flat 566) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $126.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.70** / 初期 $100.00 (+0.70%)
- 確定: 297件 (Win 98 / Loss 133 / Flat 66) / pending 5件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.70

## 6. Latest Market Context

- 更新: 2026-07-20T08:36:17.186969+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64235.4
- Funnel: target 884 → liquid 139 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 89.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +104.60% | $12,738,159.05 |
| BANK/USDT:USDT | +53.39% | $108,495,780.59 |
| EVAA/USDT:USDT | +29.22% | $5,318,582.38 |
| PROM/USDT:USDT | +23.52% | $2,949,634.83 |
| PUMPFUN/USDT:USDT | +18.07% | $25,331,746.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.01% | +3.03% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.38% | +2.41% |
| SOXL/USDT:USDT | below_1h_threshold | +2.34% | +2.36% |
| KAITO/USDT:USDT | below_1h_threshold | +1.95% | +1.97% |
| PENGU/USDT:USDT | below_1h_threshold | +1.35% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
